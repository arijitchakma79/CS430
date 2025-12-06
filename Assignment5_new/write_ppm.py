import sys

def write_ppm(framebuffer, maxval, output=sys.stdout):
    height = len(framebuffer)
    width = len(framebuffer[0]) if height > 0 else 0
    
    output.write("P3\n")
    output.write(f"{width} {height}\n")
    output.write(f"{maxval}\n")

    for y in range(height):
        row_values = []
        for x in range(width):
            r, g, b = framebuffer[y][x]
            row_values.append(f"{r} {g} {b}")
        output.write(" ".join(row_values) + "\n")
    
    output.flush()