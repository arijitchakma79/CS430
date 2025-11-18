def parse_smf(filename):
    vertices_world = [(0.0, 0.0, 0.0)]  
    edges = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                if not parts:
                    continue
                cmd = parts[0]
                if cmd == "v" and len(parts) >= 4:
                    try:
                        x = float(parts[1])
                        y = float(parts[2])
                        z = float(parts[3])
                        vertices_world.append((x, y, z))
                    except ValueError:
                        continue 
                elif cmd == "f" and len(parts) >= 3:
                    face_indices = []
                    for p in parts[1:]:
                        try:
                            face_indices.append(int(p))
                        except ValueError:
                            pass  

                    if len(face_indices) >= 2:
                        # make edges in a loop
                        for i in range(len(face_indices)):
                            v1 = face_indices[i]
                            v2 = face_indices[(i + 1) % len(face_indices)]
                            edges.append((v1, v2))
                else:
                    continue

    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open SMF file: {filename}")

    return vertices_world, edges

