class ParsePS:
    @staticmethod
    def parse_ps_input(filepath):
        commands = []         
        inside_block = False
        current_moveto = None   

        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("%%%BEGIN"):
                    inside_block = True
                    continue

                if line.startswith("%%%END"):
                    inside_block = False
                    continue

                if not inside_block:
                    continue

                parts = line.split()

                if len(parts) == 3 and parts[2] == "moveto":
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        current_moveto = (x, y)
                        commands.append({
                            "type": "moveto",
                            "P0": current_moveto
                        })
                    except ValueError:
                        continue
                    continue


                if len(parts) == 3 and parts[2] == "lineto":
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        commands.append({
                            "type": "lineto",
                            "P": (x, y)
                        })
                    except ValueError:
                        continue
                    continue

                if len(parts) == 7 and parts[6] == "curveto":
                    try:
                        x1 = float(parts[0])
                        y1 = float(parts[1])
                        x2 = float(parts[2])
                        y2 = float(parts[3])
                        x3 = float(parts[4])
                        y3 = float(parts[5])

                        if current_moveto is None:
                            continue

                        commands.append({
                            "type": "curveto",
                            "P0": current_moveto,
                            "P1": (x1, y1),
                            "P2": (x2, y2),
                            "P3": (x3, y3)
                        })

                        current_moveto = (x3, y3)

                    except ValueError:
                        continue
                    continue

                if len(parts) == 1 and parts[0] == "stroke":
                    commands.append({"type": "stroke"})
                    continue

                # Handle Line procedure: x1 y1 x2 y2 Line
                if len(parts) == 5 and parts[4] == "Line":
                    try:
                        x1 = float(parts[0])
                        y1 = float(parts[1])
                        x2 = float(parts[2])
                        y2 = float(parts[3])
                        # Line procedure does: moveto, lineto, stroke
                        commands.append({
                            "type": "moveto",
                            "P0": (x1, y1)
                        })
                        commands.append({
                            "type": "lineto",
                            "P": (x2, y2)
                        })
                        commands.append({"type": "stroke"})
                        current_moveto = (x2, y2)
                    except ValueError:
                        continue
                    continue

                continue
        return commands

    @staticmethod
    def ps_write(polylines, width, height):
        output = []
        output.append(f"<< /PageSize [{width} {height}] >> setpagedevice")
        output.append("0.25 setlinewidth")

        for poly in polylines:
            if len(poly) < 2:
                continue

            x0, y0 = poly[0]
            output.append(f"{x0:.2f} {y0:.2f} moveto")

            for (x, y) in poly[1:]:
                output.append(f"{x:.2f} {y:.2f} lineto")

            output.append("stroke")

        output.append("showpage")
        return "\n".join(output)

    @staticmethod
    def write_ps_file(polylines, width, height, outpath):
        content = ParsePS.ps_write(polylines, width, height)
        # Write as ASCII-safe text
        with open(outpath, "w", encoding="ascii", errors="ignore") as f:
            f.write(content)

if __name__ == "__main__":
    filepath = 'ExtraCredit.ps'
    parse_ps = ParsePS.parse_ps_input(filepath)
    print(parse_ps)