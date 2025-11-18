import sys

def world_to_viewport(xw, yw, a, b, c, d, j, k, o, p):
    sx = (o - j) / (c - a)
    sy = (p - k) / (d - b)
    xv = j + (xw - a) * sx
    yv = k + (yw - b) * sy
    return xv, yv

def write_pbm(fb, width, height):
    sys.stdout.reconfigure(encoding='ascii')  
    print("P1")
    print(f"{width} {height}")
    for y in range(height - 1, -1, -1): 
        print(" ".join(str(fb[y][x]) for x in range(width)))