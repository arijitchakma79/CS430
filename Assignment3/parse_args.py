import sys

def parse_args(argv):
    options = {}
    i = 1
    while i < len(argv):
        token = argv[i]
        if (token.startswith("-") 
            and len(token) == 2 
            and token[1] in "fsrmnabcdjkop"):
            
            key = token[1]
            if i + 1 >= len(argv):
                print(f"Value missing for {token}", file=sys.stderr)
                sys.exit(1)
            val = argv[i + 1]
            try:
                if key == "f":
                    options[key] = val
                elif key == "s":
                    options[key] = float(val)
                elif key in ["r", "m", "n", "a", "b", "c", "d", "j", "k", "o", "p"]:
                    options[key] = int(val)
            except ValueError:
                print(f"Invalid value for {token}: {val}", file=sys.stderr)
                sys.exit(1)
            i += 2
        else:
            print(f"Ignoring unrecognized argument: {token}", file=sys.stderr)
            i += 1
    options["f"] = options.get("f", "hw3_split.ps")
    options["s"] = options.get("s", 1.0)
    options["r"] = options.get("r", 0)
    options["m"] = options.get("m", 0)
    options["n"] = options.get("n", 0)
    options["a"] = options.get("a", 0)
    options["b"] = options.get("b", 0)
    options["c"] = options.get("c", 250)
    options["d"] = options.get("d", 250)
    options["j"] = options.get("j", 0)
    options["k"] = options.get("k", 0)
    options["o"] = options.get("o", 200)
    options["p"] = options.get("p", 200)

    # Validate bounds
    if options["a"] >= options["c"] or options["b"] >= options["d"]:
        print("Invalid world window bounds: must have a < c and b < d", file=sys.stderr)
        sys.exit(1)
    if options["j"] < 0 or options["k"] < 0 or options["o"] > 500 or options["p"] > 500:
        print("Viewport bounds must be between 0 and 500", file=sys.stderr)
        sys.exit(1)
    if options["j"] >= options["o"] or options["k"] >= options["p"]:
        print("Invalid viewport bounds: must have j < o and k < p", file=sys.stderr)
        sys.exit(1)

    return options
