from parse_args import parse_args
from parse_ps import ParsePS
from transform import Transform
from cohen_sutherland import CohenSutherland
import sys

def main():
    args = parse_args(sys.argv)

    # Step 1: Read input lines
    input_lines = ParsePS.parse_ps_input(args["f"])

    # Step 2: Create transformation matrix
    transform = Transform()
    transform.scale(args["s"], args["s"])
    transform.rotate(args["r"])
    transform.translate(args["m"], args["n"])

    # Step 3: Setup world window clipping
    clipper = CohenSutherland(args["a"], args["b"], args["c"], args["d"])

    # Step 4: Process lines (transform → clip → screen coords)
    processed_lines = []

    for (x1, y1, x2, y2) in input_lines:
        # Apply transformation to both points
        tx1, ty1 = transform.apply(x1, y1)
        tx2, ty2 = transform.apply(x2, y2)

        # Clip the line
        clipped = clipper.clip_line(tx1, ty1, tx2, ty2)

        if clipped:
            cx1, cy1, cx2, cy2 = clipped

            # Translate to screen coordinates by subtracting window origin
            sx1 = cx1 - args["a"]
            sy1 = cy1 - args["b"]
            sx2 = cx2 - args["a"]
            sy2 = cy2 - args["b"]

            processed_lines.append((sx1, sy1, sx2, sy2))
        else:
            print(f"Clipped: ({x1:.2f}, {y1:.2f}) → ({x2:.2f}, {y2:.2f})", file=sys.stderr)

    # Step 5: Generate Postscript output
    xsize = args["c"] - args["a"] + 1
    ysize = args["d"] - args["b"] + 1

    ps_output = ParsePS.parse_ps_output(processed_lines, (xsize, ysize))
    print(ps_output)

if __name__ == "__main__":
    main()
