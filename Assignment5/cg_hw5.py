import numpy as np
import sys
sys.stdout.reconfigure(encoding='ascii')

from parse_args import parse_args
from parse_smf import parse_smf
import transform_vrc
from transform_vrc import build_vrc_transform
print("[DEBUG] Using transform_vrc file:", transform_vrc.__file__, file=sys.stderr)
from projection import project_vertices
from ncp_mapping import npc_mapping
from scanline import scanline
from z_buffer import z_buffer_update
from parse_ppm import write_ppm


def main(args):

    # ------------------------------------
    # LOAD MODELS WITH BASE COLORS
    # ------------------------------------
    models = []

    if args["f"] is not None:
        verts, faces = parse_smf(args["f"])
        models.append((verts, faces, (args["maxval"], 0, 0)))   # red
        print("[DEBUG] Loaded model -f:", args["f"], "verts:", len(verts), "faces:", len(faces), file=sys.stderr)

    if args["g"] is not None:
        verts, faces = parse_smf(args["g"])
        models.append((verts, faces, (0, args["maxval"], 0)))   # green
        print("[DEBUG] Loaded model -g:", args["g"], "verts:", len(verts), "faces:", len(faces), file=sys.stderr)

    if args["i"] is not None:
        verts, faces = parse_smf(args["i"])
        models.append((verts, faces, (0, 0, args["maxval"])))   # blue
        print("[DEBUG] Loaded model -i:", args["i"], "verts:", len(verts), "faces:", len(faces), file=sys.stderr)

    width  = args["o"]
    height = args["p"]

    framebuffer = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]
    zbuffer     = [[1.0 for _ in range(width)]       for _ in range(height)]

    # ------------------------------------
    # CAMERA
    # ------------------------------------
    VRP = np.array([args["x"], args["y"], args["z"]], float)
    CW  = np.array([args["X"], args["Y"], args["Z"]], float)
    VPN = CW - VRP

    print("\n===== CAMERA DEBUG =====", file=sys.stderr)
    print("VRP:", VRP, file=sys.stderr)
    print("CW :", CW, file=sys.stderr)
    print("VPN:", VPN, file=sys.stderr)
    print("Window u,v:", args["u"], args["v"], "U,V:", args["U"], args["V"], file=sys.stderr)
    print("Near F:", args["F"], "Far B:", args["B"], file=sys.stderr)
    print("========================\n", file=sys.stderr)

    M_view = build_vrc_transform(VRP, VPN, (args["q"], args["r"], args["w"]))

    # ------------------------------------
    # USER NEAR/FAR + WINDOW
    # ------------------------------------
    F_plane = args["F"]
    B_plane = args["B"]

    umin = args["u"]
    umax = args["U"]
    vmin = args["v"]
    vmax = args["V"]
    filename = args["outfile"]
    print("Output File: ", filename, file=sys.stderr)

    total_pixels_written = 0

    # ------------------------------------
    # RENDER EACH MODEL
    # ------------------------------------
    for (verts_wc, faces, base_color) in models:

        print("\n================ MODEL START ================", file=sys.stderr)

        # 1. WORLD → VRC
        verts_vrc = []
        for vx, vy, vz in verts_wc:
            u, v, n, _ = np.array([vx, vy, vz, 1.0], float) @ M_view
            verts_vrc.append((u, v, n))

        print("[DEBUG] First 5 VRC vertices:", verts_vrc[:5], file=sys.stderr)

        # Print VRC z range
        zvals = [n for (_, _, n) in verts_vrc]
        print("[DEBUG] VRC z-range:", min(zvals), max(zvals), file=sys.stderr)

        # 2. PROJECTION
        verts_proj = project_vertices(
            verts_vrc,
            PRP=(args["Q"], args["R"], args["W"]),
            parallel=args["P"],
            F=F_plane
        )

        xs = [x for (x,_,_) in verts_proj]
        ys = [y for (_,y,_) in verts_proj]

        print("[DEBUG] Projection x-range:", min(xs), max(xs), file=sys.stderr)
        print("[DEBUG] Projection y-range:", min(ys), max(ys), file=sys.stderr)

        # 3. NPC MAPPING
        verts_npc = npc_mapping(
            verts_proj,
            umin=umin, umax=umax,
            vmin=vmin, vmax=vmax,
            F=F_plane, B=B_plane
        )

        xn = [x for (x,_,_) in verts_npc]
        yn = [y for (_,y,_) in verts_npc]
        zn = [z for (_,_,z) in verts_npc]

        print("[DEBUG] NPC x-range:", min(xn), max(xn), file=sys.stderr)
        print("[DEBUG] NPC y-range:", min(yn), max(yn), file=sys.stderr)
        print("[DEBUG] NPC z-range:", min(zn), max(zn), file=sys.stderr)

        # 4. NPC → SCREEN
        verts_screen = []
        for (xn, yn, zn) in verts_npc:
            sx = int((xn + 1) * 0.5 * (width - 1))
            sy = int((1 - (yn + 1) * 0.5) * (height - 1))
            verts_screen.append((sx, sy, zn))

        xs2 = [sx for (sx,_,_) in verts_screen]
        ys2 = [sy for (_,sy,_) in verts_screen]
        print("[DEBUG] SCREEN x-range:", min(xs2), max(xs2), file=sys.stderr)
        print("[DEBUG] SCREEN y-range:", min(ys2), max(ys2), file=sys.stderr)

        # 5. TRIANGLES → SCANLINE → Z-BUFFER
        tri_count = 0
        pixel_count_model = 0

        for (i1, i2, i3) in faces:

            tri_count += 1

            # VRC z for clipping
            (_,_,n1) = verts_vrc[i1]
            (_,_,n2) = verts_vrc[i2]
            (_,_,n3) = verts_vrc[i3]

            if (n1 < B_plane or n1 > F_plane or
                n2 < B_plane or n2 > F_plane or
                n3 < B_plane or n3 > F_plane):

                continue

            v1s = verts_screen[i1]
            v2s = verts_screen[i2]
            v3s = verts_screen[i3]

            pixels = scanline((v1s, v2s, v3s), width, height)

            if len(pixels) == 0:
                print("[DEBUG] Empty triangle fill at screen verts:", v1s, v2s, v3s, file=sys.stderr)
                continue

            # Update z-buffer
            for (x, y, z_npc) in pixels:
                before = zbuffer[y][x]
                z_buffer_update(x, y, z_npc, zbuffer, framebuffer, base_color,
                                F_plane, B_plane)
                after = zbuffer[y][x]
                if after != before:
                    total_pixels_written += 1
                    pixel_count_model += 1

        print("[DEBUG] Triangles processed:", tri_count, file=sys.stderr)
        print("[DEBUG] Pixels written for model:", pixel_count_model, file=sys.stderr)

    print("\n================ FINAL DEBUG ================", file=sys.stderr)
    print("[DEBUG] Total pixels written:", total_pixels_written, file=sys.stderr)
    print("============================================\n", file=sys.stderr)

    write_ppm(filename, framebuffer, args["maxval"])


if __name__ == "__main__":
    args = parse_args()
    print("[DEBUG] Parsed arguments - j:", args["j"], "k:", args["k"], "o:", args["o"], "p:", args["p"], "f:", args["f"], file=sys.stderr)
    main(args)
