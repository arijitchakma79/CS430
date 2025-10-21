import sys
from parse_args import parse_args
from parse_ps import ParsePS
from transform import Transform
from algorithm import SutherlandHodgma

def main():
    args = parse_args(sys.argv)
    vertices = ParsePS.parse_ps_input(args["f"])
    t = Transform()
    if args["s"] != 1.0:
        t.scale(args["s"], args["s"])
    if args["r"] != 0:
        t.rotate(args["r"])
    if args["m"] != 0 or args["n"] != 0:
        t.translate(args["m"], args["n"])
    transformed = t.apply_to_vertices(vertices)
    clipper = SutherlandHodgman(args["a"], args["b"], args["c"], args["d"])
    clipped = clipper.clip(transformed)
    ps_output = ParsePS.parse_ps_output(clipped, (500, 500))
    print(ps_output)

if __name__ == "__main__":
    main()