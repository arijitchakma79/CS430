import sys

def parse_args():
    args = sys.argv[1:]
    cfg = {
        "f": "bound-sprellpsd.smf",
        "g": None,
        "i": None,
        "F": 0.6,
        "B": -0.6,
        "j": 0,
        "k": 0,
        "o": 500,
        "p": 500,
        "x": 0.0,
        "y": 0.0,
        "z": 1.0,
        "X": 0.0,
        "Y": 0.0,
        "Z": 0.0,
        "q": 0.0,
        "r": 0.0,
        "w": -1.0,
        "Q": 0.0,
        "R": 1.0,
        "W": 0.0,
        "u": -0.7,
        "v": -0.7,
        "U": 0.7,
        "V": 0.7,
        "P": False
    }

    i = 0
    while i < len(args):
        a = args[i]

        if a == "-F" and i+1 < len(args):
            cfg["F"] = float(args[i+1])
            i += 2
            continue

        if a == "-B" and i+1 < len(args):
            cfg["B"] = float(args[i+1])
            i += 2
            continue

        if a == "-f" and i+1 < len(args):
            cfg["f"] = args[i+1]
            i += 2
            continue

        if a == "-g" and i+1 < len(args):
            cfg["g"] = args[i+1]
            i += 2
            continue

        if a == "-i" and i+1 < len(args):
            cfg["i"] = args[i+1]
            i += 2
            continue

        if a == "-j" and i+1 < len(args):
            cfg["j"] = int(args[i+1])
            i += 2
            continue

        if a == "-k" and i+1 < len(args):
            cfg["k"] = int(args[i+1])
            i += 2
            continue

        if a == "-o" and i+1 < len(args):
            cfg["o"] = int(args[i+1])
            i += 2
            continue

        if a == "-p" and i+1 < len(args):
            cfg["p"] = int(args[i+1])
            i += 2
            continue

        if a == "-x" and i+1 < len(args):
            cfg["x"] = float(args[i+1])
            i += 2
            continue

        if a == "-y" and i+1 < len(args):
            cfg["y"] = float(args[i+1])
            i += 2
            continue

        if a == "-z" and i+1 < len(args):
            cfg["z"] = float(args[i+1])
            i += 2
            continue

        if a == "-X" and i+1 < len(args):
            cfg["X"] = float(args[i+1])
            i += 2
            continue

        if a == "-Y" and i+1 < len(args):
            cfg["Y"] = float(args[i+1])
            i += 2
            continue

        if a == "-Z" and i+1 < len(args):
            cfg["Z"] = float(args[i+1])
            i += 2
            continue

        if a == "-q" and i+1 < len(args):
            cfg["q"] = float(args[i+1])
            i += 2
            continue

        if a == "-r" and i+1 < len(args):
            cfg["r"] = float(args[i+1])
            i += 2
            continue

        if a == "-w" and i+1 < len(args):
            cfg["w"] = float(args[i+1])
            i += 2
            continue

        if a == "-Q" and i+1 < len(args):
            cfg["Q"] = float(args[i+1])
            i += 2
            continue

        if a == "-R" and i+1 < len(args):
            cfg["R"] = float(args[i+1])
            i += 2
            continue

        if a == "-W" and i+1 < len(args):
            cfg["W"] = float(args[i+1])
            i += 2
            continue

        if a == "-u" and i+1 < len(args):
            cfg["u"] = float(args[i+1])
            i += 2
            continue

        if a == "-v" and i+1 < len(args):
            cfg["v"] = float(args[i+1])
            i += 2
            continue

        if a == "-U" and i+1 < len(args):
            cfg["U"] = float(args[i+1])
            i += 2
            continue

        if a == "-V" and i+1 < len(args):
            cfg["V"] = float(args[i+1])
            i += 2
            continue

        if a == "-P":
            cfg["P"] = True
            i += 1
            continue

        i += 1

    if cfg["B"] >= cfg["F"]:
        print("Error: Back plane (-B) must be less than Front plane (-F).")
        sys.exit(1)

    return cfg

if __name__ == "__main__":
    print(parse_args())
