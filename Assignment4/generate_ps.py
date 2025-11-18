from cohen_sutherland import CohenSutherland

def write_postscript(edges, vertices_2d, cfg, out):
    j = cfg["j"]
    k = cfg["k"]
    o = cfg["o"]
    p = cfg["p"]
    umin = cfg["umin"]
    vmin = cfg["vmin"]
    umax = cfg["umax"]
    vmax = cfg["vmax"]

    sx = (o - j) / (umax - umin)
    sy = (p - k) / (vmax - vmin)

    clipper = CohenSutherland(umin, vmin, umax, vmax)

    print("/Line {moveto lineto stroke} bind def", file=out)
    print("1.0 setlinewidth", file=out)
    print("%%%BEGIN", file=out)

    for v1, v2 in edges:
        
        if v1 >= len(vertices_2d) or v2 >= len(vertices_2d) or v1 < 0 or v2 < 0:
            continue
        if vertices_2d[v1] is None or vertices_2d[v2] is None:
            continue
        
        u1, v1c = vertices_2d[v1]
        u2, v2c = vertices_2d[v2]

        clipped = clipper.clip_line(u1, v1c, u2, v2c)
        if clipped is None:
            continue

        cu1, cv1, cu2, cv2 = clipped

        x1 = j + (cu1 - umin) * sx
        y1 = k + (cv1 - vmin) * sy
        x2 = j + (cu2 - umin) * sx
        y2 = k + (cv2 - vmin) * sy

        print(f"{x1} {y1} {x2} {y2} Line", file=out)

    print("%%%END", file=out)
