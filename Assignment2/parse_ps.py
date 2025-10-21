class ParsePS:
    @staticmethod
    def parse_ps_input(filepath):
        vertices = []
        inside_block = False

        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()

                if line.startswith("%%%BEGIN"):
                    inside_block = True
                    continue
                if line.startswith("%%%END"):
                    inside_block = False
                    continue

                if inside_block:
                    parts = line.split()
                    if len(parts) == 3 and parts[2] in ["moveto", "lineto"]:
                        try:
                            x = float(parts[0])
                            y = float(parts[1])
                            vertices.append((x, y))
                        except ValueError:
                            continue

        return vertices

    @staticmethod
    def parse_ps_output(vertices, page_dimensions):
        width, height = page_dimensions
        output = []
        output.append("%!PS-Adobe-2.0")
        
        output.append("%%BeginSetup")
        output.append(f"<< /PageSize [{width} {height}] >> setpagedevice")
        output.append("%%EndSetup\n")
        output.append("0.1 setlinewidth\n")
        output.append("%%%BEGIN")

        if vertices:
            x0, y0 = vertices[0]
            output.append(f"{x0:.2f} {y0:.2f} moveto")
            for (x, y) in vertices[1:]:
                output.append(f"{x:.2f} {y:.2f} lineto")

            if vertices[0] != vertices[-1]:
                x0, y0 = vertices[0]
                output.append(f"{x0:.2f} {y0:.2f} lineto")

            output.append("stroke")

        output.append("%%%END")
        return "\n".join(output)
