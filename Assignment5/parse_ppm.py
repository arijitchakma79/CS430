def write_ppm(filename, framebuffer, maxval):
    height = len(framebuffer)
    width = len(framebuffer[0]) if height > 0 else 0
    
    with open(filename, "w") as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")

        for y in range(height):
            row_values = []
            for x in range(width):
                r, g, b = framebuffer[y][x]
                row_values.append(f"{r} {g} {b}")
            f.write(" ".join(row_values) + "\n")