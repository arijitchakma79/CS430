def parse_ps_input(filepath):
    lines = []
    valid = False

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith("%%%BEGIN"):
                valid = True
                continue

            if line.startswith("%%%END"):
                valid = False
                continue

            if valid:
                if not line or not line.endswith("Line"):
                    continue
                
                parts = line.split()

                if len(parts) == 5:
                    try:
                        x1 = float(parts[0])
                        y1 = float(parts[1])
                        x2 = float(parts[2])
                        y2 = float(parts[3])
                        
                        lines.append((x1,y1,x2, y2))
                    except:
                        continue

    return lines


def parse_ps_output(lines, page_dimensions):
    width, height = page_dimensions

    output = []
    output.append("%%BeginSetup")
    output.append(f"      << /PageSize [{width} {height}] >> setpagedevice")
    output.append("%%EndSetup")
    output.append("0.1 setlinewidth\n")
    output.append("%%%BEGIN")

    for (x1, y1, x2, y2) in lines:
        output.append(f"{x1:.2f} {y1:.2f} moveto")
        output.append(f"{x2:.2f} {y2:.2f} lineto")
    
    output.append("stroke")
    output.append("%%%END")
    return "\n".join(output)


if __name__ == "__main__":
    filepath = 'hw1.ps'

    # Parse input PostScript lines
    lines = parse_ps_input(filepath)
    print("Parsed lines:\n", lines)
