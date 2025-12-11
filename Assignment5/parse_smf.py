def parse_smf(filename):
    vertices_world = [(0.0, 0.0, 0.0)]
    faces = []

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split()
                if parts[0] == "v" and len(parts) >= 4:
                    x, y, z = map(float, parts[1:4])
                    vertices_world.append((x, y, z))

                elif parts[0] == "f" and len(parts) >= 4:
                    i, j, k = map(int, parts[1:4])
                    faces.append((i, j, k))

        return vertices_world, faces

    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open SMF file: {filename}")

if __name__ == "__main__":
    file = './octahedron.smf'
    print(parse_smf(file))

