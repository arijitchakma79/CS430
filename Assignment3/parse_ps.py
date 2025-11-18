class ParsePS:
    @staticmethod
    def parse_ps_input(filepath):
        polygons = []
        vertices = []
        inside_block = False
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()

                if line.startswith("%%%BEGIN"):
                    inside_block = True
                    vertices = []
                    continue
                if line.startswith("%%%END"):
                    inside_block = False
                    if vertices:
                        polygons.append(vertices)
                    vertices = []
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

        return polygons
