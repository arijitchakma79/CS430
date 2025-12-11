import sys


def parse_args():
    args_list = sys.argv[1:]
    cfg = {
        "f": "bound-sprellpsd.smf",
        "g": None,
        "i": None,
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
        "F": 0.6,
        "B": -0.6,
        "P": False,
        "maxval": 255,
        "output": sys.stdout,
        "outfile": "out.ppm"
    }

    i = 0
    L = len(args_list)
    while i < L:
        a = args_list[i]

        if a == "-f" and i+1 < L:
            cfg["f"] = args_list[i+1]
            i += 2
        elif a == "-g" and i+1 < L:
            cfg["g"] = args_list[i+1]
            i += 2
        elif a == "-i" and i+1 < L:
            cfg["i"] = args_list[i+1]
            i += 2
        elif a == "-j" and i+1 < L:
            cfg["j"] = int(args_list[i+1])
            i += 2
        elif a == "-k" and i+1 < L:
            cfg["k"] = int(args_list[i+1])
            i += 2
        elif a == "-o" and i+1 < L:
            cfg["o"] = int(args_list[i+1])
            i += 2
        elif a == "-p" and i+1 < L:
            cfg["p"] = int(args_list[i+1])
            i += 2
        elif a == "-x" and i+1 < L:
            cfg["x"] = float(args_list[i+1])
            i += 2
        elif a == "-y" and i+1 < L:
            cfg["y"] = float(args_list[i+1])
            i += 2
        elif a == "-z" and i+1 < L:
            cfg["z"] = float(args_list[i+1])
            i += 2
        elif a == "-X" and i+1 < L:
            cfg["X"] = float(args_list[i+1])
            i += 2
        elif a == "-Y" and i+1 < L:
            cfg["Y"] = float(args_list[i+1])
            i += 2
        elif a == "-Z" and i+1 < L:
            cfg["Z"] = float(args_list[i+1])
            i += 2
        elif a == "-q" and i+1 < L:
            cfg["q"] = float(args_list[i+1])
            i += 2
        elif a == "-r" and i+1 < L:
            cfg["r"] = float(args_list[i+1])
            i += 2
        elif a == "-w" and i+1 < L:
            cfg["w"] = float(args_list[i+1])
            i += 2
        elif a == "-Q" and i+1 < L:
            cfg["Q"] = float(args_list[i+1])
            i += 2
        elif a == "-R" and i+1 < L:
            cfg["R"] = float(args_list[i+1])
            i += 2
        elif a == "-W" and i+1 < L:
            cfg["W"] = float(args_list[i+1])
            i += 2
        elif a == "-u" and i+1 < L:
            cfg["u"] = float(args_list[i+1])
            i += 2
        elif a == "-v" and i+1 < L:
            cfg["v"] = float(args_list[i+1])
            i += 2
        elif a == "-U" and i+1 < L:
            cfg["U"] = float(args_list[i+1])
            i += 2
        elif a == "-V" and i+1 < L:
            cfg["V"] = float(args_list[i+1])
            i += 2
        elif a == "-F" and i+1 < L:
            cfg["F"] = float(args_list[i+1])
            i += 2
        elif a == "-B" and i+1 < L:
            cfg["B"] = float(args_list[i+1])
            i += 2
        elif a == "-P":
            cfg["P"] = True
            i += 1
        elif a == "-O" and i+1 < L:
            cfg["outfile"] = args_list[i+1]
            i += 2
        else:
            i += 1

    if cfg["B"] >= cfg["F"]:
        raise ValueError("Back plane (B) must be less than Front plane (F)")

    return cfg

if __name__ == "__main__":
    print(parse_args())

