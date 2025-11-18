def scanline_fill(polygon, fb):
    if len(polygon) < 3:
        return
    height = len(fb)
    width = len(fb[0])

    ET = [[] for _ in range(height)]
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if y1 == y2:
            continue 

        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        inv_slope = (x2 - x1) / (y2 - y1)
        ET[y1].append({"ymax": y2, "x": x1, "inv_slope": inv_slope})

    AET = []
    for y in range(height):
        for e in ET[y]:
            AET.append(e)

        AET = [e for e in AET if e["ymax"] > y]
        AET.sort(key=lambda e: e["x"])

        # Fill pairs
        for i in range(0, len(AET), 2):
            if i + 1 >= len(AET):
                break
            x_start = int(round(AET[i]["x"]))
            x_end = int(round(AET[i + 1]["x"]))
            for x in range(x_start, x_end):
                if 0 <= x < width and 0 <= y < height:
                    fb[y][x] = 1
        for e in AET:
            e["x"] += e["inv_slope"]
