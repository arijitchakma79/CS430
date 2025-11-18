import sys

def parse_args():
    args = sys.argv[1:]
    cfg = {
        "smf_file": None,
        "j": 0,
        "k": 0,
        "o": 500,
        "p": 500,
        "PRPx": 0.0,
        "PRPy": 0.0,
        "PRPz": 1.0,
        "VRP": [0.0, 0.0, 0.0],
        "VPN": [0.0, 0.0, -1.0],
        "VUP": [0.0, 1.0, 0.0],
        "umin": -0.7,
        "vmin": -0.7,
        "umax": 0.7,
        "vmax": 0.7,
        "parallel": False
    }

    i = 0
    L = len(args)
    while i < L:
        a = args[i]

        if a == "-f" and i+1 < L:
            cfg["smf_file"] = args[i+1]
            i += 2
        elif a == "-j" and i+1 < L:
            cfg["j"] = int(args[i+1])
            i += 2
        elif a == "-k" and i+1 < L:
            cfg["k"] = int(args[i+1])
            i += 2
        elif a == "-o" and i+1 < L:
            cfg["o"] = int(args[i+1])
            i += 2
        elif a == "-p" and i+1 < L:
            cfg["p"] = int(args[i+1])
            i += 2
        elif a == "-x" and i+1 < L:
            cfg["PRPx"] = float(args[i+1])
            i += 2
        elif a == "-y" and i+1 < L:
            cfg["PRPy"] = float(args[i+1])
            i += 2
        elif a == "-z" and i+1 < L:
            cfg["PRPz"] = float(args[i+1])
            i += 2
        elif a == "-X" and i+1 < L:
            cfg["VRP"][0] = float(args[i+1])
            i += 2
        elif a == "-Y" and i+1 < L:
            cfg["VRP"][1] = float(args[i+1])
            i += 2
        elif a == "-Z" and i+1 < L:
            cfg["VRP"][2] = float(args[i+1])
            i += 2
        elif a == "-q" and i+1 < L:
            cfg["VPN"][0] = float(args[i+1])
            i += 2
        elif a == "-r" and i+1 < L:
            cfg["VPN"][1] = float(args[i+1])
            i += 2
        elif a == "-w" and i+1 < L:
            cfg["VPN"][2] = float(args[i+1])
            i += 2
        elif a == "-Q" and i+1 < L:
            cfg["VUP"][0] = float(args[i+1])
            i += 2
        elif a == "-R" and i+1 < L:
            cfg["VUP"][1] = float(args[i+1])
            i += 2
        elif a == "-W" and i+1 < L:
            cfg["VUP"][2] = float(args[i+1])
            i += 2
        elif a == "-u" and i+1 < L:
            cfg["umin"] = float(args[i+1])
            i += 2
        elif a == "-v" and i+1 < L:
            cfg["vmin"] = float(args[i+1])
            i += 2
        elif a == "-U" and i+1 < L:
            cfg["umax"] = float(args[i+1])
            i += 2
        elif a == "-V" and i+1 < L:
            cfg["vmax"] = float(args[i+1])
            i += 2
        elif a == "-P":
            cfg["parallel"] = True
            i += 1
        else:
            i += 1

    if cfg["smf_file"] is None:
        raise ValueError("SMF file not specified with -f")

    return cfg

if __name__ == "__main__":
    print(parse_args())
