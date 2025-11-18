import sys
from parse_args import parse_args
from parse_ps import ParsePS
from transform import Transform
from sutherland_hodgman import SutherlandHodgman
from scanline import scanline_fill
from helper import world_to_viewport, write_pbm

def main():
    args = parse_args(sys.argv)
    polygons = ParsePS.parse_ps_input(args["f"])
    fb = [[0 for _ in range(501)] for _ in range(501)]
    for vertices in polygons:
        t = Transform()
        t.scale(args["s"], args["s"])
        t.rotate(args["r"])
        t.translate(args["m"], args["n"])
        transformed = t.apply_to_vertices(vertices)

        clipper = SutherlandHodgman(args["a"], args["b"], args["c"], args["d"])
        clipped = clipper.clip(transformed)
        if not clipped:
            continue

        # Map to viewport
        mapped = [world_to_viewport(x, y,
                                    args["a"], args["b"], args["c"], args["d"],
                                    args["j"], args["k"], args["o"], args["p"])
                  for (x, y) in clipped]

        # Round to integer pixel coords
        rounded = [(int(round(x)), int(round(y))) for (x, y) in mapped]

        # Fill polygon
        scanline_fill(rounded, fb)

    # Output PBM image
    write_pbm(fb, 501, 501)

if __name__ == "__main__":
    main()