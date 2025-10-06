import sys

def parse_args(argv):
    options = {}
    i = 1
    while i < len(argv):
        token = argv[i]
        if token.startswith("-") and len(token) == 2 and token[1] in "fsrmnabcd":
            key = token[1]
            if i + 1 >= len(argv):
                print(f"Value missing for {token}")
                sys.exit(1)
            val = argv[i + 1]
            try:
                if key == "f":
                    options[key] = val
                elif key == "s":
                    options[key] = float(val)
                elif key in ["r", "m", "n", "a", "b", "c", "d"]:
                    options[key] = int(val)
            except ValueError:
                print(f"Invalid value for {token}: {val}")
                sys.exit(1)
            i += 2
        else:
            print(f"Ignoring unrecognized argument: {token}")
            i += 1

    options["f"] = options.get("f", "hw1.ps")
    options["s"] = options.get("s", 1.0)
    options["r"] = options.get("r", 0)
    options["m"] = options.get("m", 0)
    options["n"] = options.get("n", 0)
    options["a"] = options.get("a", 0)
    options["b"] = options.get("b", 0)
    options["c"] = options.get("c", 499)
    options["d"] = options.get("d", 499)

    if options["a"] >= options["c"] or options["b"] >= options["d"]:
        print("Invalid window bounds: must have a < c and b < d")
        sys.exit(1)

    return options


if __name__ == "__main__":
    args = parse_args(sys.argv)
    print(args)
