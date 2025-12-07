

import sys
from parse_args import parse_args
from parse_ps import ParsePS
from BezierCurve import BezierCurve
from transform import Transform
from cohen_sutherland import CohenSutherland
from viewportMap import ViewportMapper
from clip_polyline import clip_polyline


def main():
    args = parse_args(sys.argv)

    commands = ParsePS.parse_ps_input(args["f"])
    bezier = BezierCurve(args["N"])
    T = Transform()
    T.scale(args["s"], args["s"])
    T.rotate(args["r"])
    T.translate(args["m"], args["n"])

    clipper = CohenSutherland(args["a"],args["b"],args["c"],args["d"])
    viewport = ViewportMapper(args["a"],args["b"],args["c"],args["d"], args["j"],args["k"],args["o"],args["p"])
    polylines=[]
    current_poly=None
    for cmd in commands:
        if cmd["type"]=="moveto":
            current_poly=[]
            start = cmd["P0"]
            current_poly.append(start)

        elif cmd["type"]=="lineto":
            current_poly.append(cmd["P"])

        elif cmd["type"]=="curveto":
            P0 = cmd["P0"]
            P1 = cmd["P1"]
            P2 = cmd["P2"]
            P3 = cmd["P3"]
            curve_poly = bezier.bezier_to_polyline(P0,P1,P2,P3)
            if current_poly is None:
                current_poly = [curve_poly[0]]  
            current_poly.extend(curve_poly[1:])

        elif cmd["type"]=="stroke":
            if current_poly and len(current_poly)>1:
                transformed=[T.apply(x,y) for (x,y) in current_poly]
                clipped = clip_polyline(transformed,clipper)
                if len(clipped) >= 2:
                    mapped=[viewport.map(x,y) for (x,y) in clipped]
                    polylines.append(mapped)

            current_poly=None

    width =501 
    height = 501 
    
    print(ParsePS.ps_write(polylines, width, height))


if __name__=="__main__":
    main()