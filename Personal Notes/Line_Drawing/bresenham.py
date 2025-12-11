import matplotlib.pyplot as plt

def drawLineH(x0, y0, x1, y1, putPixel):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    dir = -1 if dy < 0 else 1
    dy *= dir

    if dx != 0:
        y = y0
        p = 2*dy - dx
        for i in range(dx + 1):
            putPixel(x0 + i, y)
            if p >= 0:
                y += dir
                p -= 2*dx
            p += 2*dy


def drawLineV(x0, y0, x1, y1, putPixel):
    if y0 > y1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    dir = -1 if dx < 0 else 1
    dx *= dir

    if dy != 0:
        x = x0
        p = 2*dx - dy
        for i in range(dy + 1):
            putPixel(x, y0 + i)
            if p >= 0:
                x += dir
                p -= 2*dy
            p += 2*dx


def bresenham(x0, y0, x1, y1):
    pixels = []

    def putPixel(x, y):
        pixels.append((x, y))

    if abs(y1 - y0) <= abs(x1 - x0):
        drawLineH(x0, y0, x1, y1, putPixel)
    else:
        drawLineV(x0, y0, x1, y1, putPixel)

    return pixels


# Example points
q = (2, 3)
r = (12, 8)

# Compute Bresenham pixels
pixels = bresenham(q[0], q[1], r[0], r[1])

# Extract X and Y for plotting
xs = [p[0] for p in pixels]
ys = [p[1] for p in pixels]

# Plot
plt.figure(figsize=(6, 6))
plt.scatter(xs, ys, marker='s', s=100)       # pixel squares
plt.plot([q[0], r[0]], [q[1], r[1]])         # true line for reference

plt.gca().invert_yaxis()                     # optional (to match screen coords)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.title("Bresenham Line Drawing")
plt.show()
