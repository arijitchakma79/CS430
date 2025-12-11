import math

def scanline(triangle, width, height):
    """
    triangle = [(x0,y0,z0), (x1,y1,z1), (x2,y2,z2)]
    x, y are pixel coords.
    z is NPC depth in [0, 1].

    Returns: list of (x, y, z) samples.
    """

    pixels = []
    ET = [[] for _ in range(height)]

    # Build edge table
    for i in range(3):
        x1, y1, z1 = triangle[i]
        x2, y2, z2 = triangle[(i + 1) % 3]

        if y1 > y2:
            x1, y1, z1, x2, y2, z2 = x2, y2, z2, x1, y1, z1

        ymin = math.ceil(y1)
        ymax = math.ceil(y2)

        if ymin == ymax:
            continue

        dy = y2 - y1
        dxdy = (x2 - x1) / dy
        dzdy = (z2 - z1) / dy

        if ymax <= 0 or ymin >= height:
            continue

        start_y = max(0, ymin)
        y_offset = start_y - y1
        start_x = x1 + dxdy * y_offset
        start_z = z1 + dzdy * y_offset

        ymax_clamped = min(ymax, height)

        ET[start_y].append({
            "ymax": ymax_clamped,
            "x": start_x,
            "z": start_z,
            "dx": dxdy,
            "dz": dzdy
        })

    # Fill
    AET = []

    for y in range(height):

        for entry in ET[y]:
            AET.append(entry)

        AET = [e for e in AET if e["ymax"] > y]
        AET.sort(key=lambda e: e["x"])

        for i in range(0, len(AET), 2):
            if i + 1 >= len(AET):
                break

            L = AET[i]
            R = AET[i + 1]

            xL, zL = L["x"], L["z"]
            xR, zR = R["x"], R["z"]

            if xR <= xL:
                continue

            start_x = max(0, int(math.floor(xL)))
            end_x   = min(width - 1, int(math.floor(xR)))

            denom = (xR - xL)
            for x in range(start_x, end_x + 1):
                t = (x - xL) / denom
                z = zL + t * (zR - zL)
                pixels.append((x, y, z))

        for e in AET:
            e["x"] += e["dx"]
            e["z"] += e["dz"]

    return pixels
