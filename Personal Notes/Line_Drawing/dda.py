import matplotlib.pyplot as plt

def dda(q, r):
    x0, y0 = q
    x1, y1 = r
    dx, dy = x1 - x0, y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0
    pixels = []

    for _ in range(steps + 1):
        pixels.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    
    return pixels

if __name__ == "__main__":
    # Example points
    q = (2, 3)
    r = (12, 8)

    # Generate pixels
    pixels = dda(q, r)

    # Extract for plotting
    xs = [p[0] for p in pixels]
    ys = [p[1] for p in pixels]

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, marker='s', s=100)       # DDA pixels
    plt.plot([q[0], r[0]], [q[1], r[1]])         # real line

    plt.gca().invert_yaxis()                     # optional for screen coords
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title("DDA Line Drawing Algorithm")
    plt.show()

