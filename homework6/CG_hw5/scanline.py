from z_buffer import z_buffer_update

def scanline_fill_triangle(tri, framebuffer, zbuffer, base_color, F, B):
    (x0, y0, z0), (x1, y1, z1), (x2, y2, z2) = tri
    h = len(framebuffer)
    w = len(framebuffer[0])

    ET = [[] for _ in range(h)]
    verts = [(x0, y0, z0), (x1, y1, z1), (x2, y2, z2)]

    for i in range(3):
        x1, y1, z1 = verts[i]
        x2, y2, z2 = verts[(i + 1) % 3]

        if y1 == y2:
            continue

        if y1 > y2:
            x1, y1, z1, x2, y2, z2 = x2, y2, z2, x1, y1, z1

        dy = y2 - y1
        dx = (x2 - x1) / dy
        dz = (z2 - z1) / dy

        y1i = int(y1)
        ymax = int(y2)

        if ymax < 0 or y1i >= h:
            continue

        y1i_clamped = max(y1i, 0)
        if y1i_clamped != y1i:
            shift = (y1i_clamped - y1) 
            x1 = x1 + dx * shift
            z1 = z1 + dz * shift
            y1i = y1i_clamped

        if 0 <= y1i < h:
            ET[y1i].append({
                "ymax": ymax,
                "x": x1,
                "z": z1,
                "dx": dx,
                "dz": dz
            })

    AET = []

    for y in range(h):
        for e in ET[y]:
            AET.append(e)

        AET = [e for e in AET if e["ymax"] > y]

        AET.sort(key=lambda e: e["x"])

        for i in range(0, len(AET), 2):
            if i + 1 >= len(AET):
                break

            L = AET[i]
            R = AET[i + 1]

            x_start = int(L["x"])
            x_end = int(R["x"])

            if x_end == x_start:
                continue

            z = L["z"]
            dzdx = (R["z"] - L["z"]) / (x_end - x_start)

            for x in range(x_start, x_end):
                if 0 <= x < w:
                    z_buffer_update(x, y, z, zbuffer, framebuffer, base_color, F, B)
                z += dzdx

        for e in AET:
            e["x"] += e["dx"]
            e["z"] += e["dz"]
