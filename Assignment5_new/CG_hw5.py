import sys
sys.stdout.reconfigure(encoding='ascii')

from parse_args import parse_args
from parse_smf import parse_smf
from project3D_to_2D import Project3D_to_2D
from scanline import scanline_fill_triangle
from write_ppm import write_ppm
import math


def main():
    cfg = parse_args()
    print("[DEBUG] Parsed args:", cfg, file=sys.stderr)

    models = []
    if cfg["f"]:
        print(f"[DEBUG] Loading model -f {cfg['f']}", file=sys.stderr)
        verts, faces = parse_smf(cfg["f"])
        models.append(("red", verts, faces))

    if cfg["g"]:
        print(f"[DEBUG] Loading model -g {cfg['g']}", file=sys.stderr)
        verts, faces = parse_smf(cfg["g"])
        models.append(("green", verts, faces))

    if cfg["i"]:
        print(f"[DEBUG] Loading model -i {cfg['i']}", file=sys.stderr)
        verts, faces = parse_smf(cfg["i"])
        models.append(("blue", verts, faces))

    width = cfg["o"]
    height = cfg["p"]
    print(f"[DEBUG] Framebuffer {width}x{height}", file=sys.stderr)

    framebuffer = [[(0,0,0) for _ in range(width)] for _ in range(height)]
    zbuffer = [[float("inf") for _ in range(width)] for _ in range(height)]
    print("[DEBUG] Buffers initialized", file=sys.stderr)

    projector = Project3D_to_2D(cfg)
    print("[DEBUG] Projector initialized", file=sys.stderr)

    for color, verts, faces in models:
        if color == "red":
            base_color = (255, 0, 0)
        elif color == "green":
            base_color = (0, 255, 0)
        else:
            base_color = (0, 0, 255)

        print(f"[DEBUG] Rendering model color={color}", file=sys.stderr)

        for f in faces:
            i1, i2, i3 = f
            v1 = verts[i1]
            v2 = verts[i2]
            v3 = verts[i3]

            x1, y1, z1 = projector.project_vertex(v1)
            x2, y2, z2 = projector.project_vertex(v2)
            x3, y3, z3 = projector.project_vertex(v3)

            print(f"[DEBUG] Face {f} -> P1={x1,y1,z1} P2={x2,y2,z2} P3={x3,y3,z3}",
                  file=sys.stderr)

            tri = ((x1, y1, z1),
                   (x2, y2, z2),
                   (x3, y3, z3))

            if (
                math.isnan(x1) or math.isnan(y1) or math.isnan(z1) or
                math.isnan(x2) or math.isnan(y2) or math.isnan(z2) or
                math.isnan(x3) or math.isnan(y3) or math.isnan(z3) or
                math.isinf(x1) or math.isinf(y1) or math.isinf(z1) or
                math.isinf(x2) or math.isinf(y2) or math.isinf(z2) or
                math.isinf(x3) or math.isinf(y3) or math.isinf(z3)
            ):
                print("[DEBUG] Skipping triangle with invalid projected vertex", file=sys.stderr)
                continue

            scanline_fill_triangle(tri, framebuffer, zbuffer, base_color,
                                   cfg["F"], cfg["B"])

    print("[DEBUG] Rendering complete", file=sys.stderr)
    try:
        write_ppm(framebuffer, 255, sys.stdout)
    except Exception as e:
        print(f"[ERROR] Failed to write PPM: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
