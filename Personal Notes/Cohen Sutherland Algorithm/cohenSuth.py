# Cohen–Sutherland region codes

INSIDE = 0 # 0000
TOP = 1 << 3    # 1000
BOTTOM = 1 << 2 # 0100
RIGHT = 1 << 1  # 0010
LEFT = 1 << 0   # 0001

def compute_code(x, y, WL, WR, WB, WT):
    code = INSIDE
    if y > WT:
        code |= TOP
    elif y < WB:
        code |= BOTTOM
    if x > WR:
        code |= RIGHT
    elif x < WL:
        code |= LEFT
    return code

def cohen_sutherland_clip(x0, x1, y0, y1, WL, WR, WB, WT):
    code0 = compute_code(x0, y0, WL, WR, WB, WT)
    code01 = compute_code(x1, y1, WL, WR, WB, WT)

    while True:
        # Trivial accept
        if code0 == 0 and code01 == 0:
            return True, (x0, y0, x1, y1)
        # Trivial Reject
        if code0 & code01 != 0:
            return False, None
        
        # Clip one endpoint
        if code0 != 0:
            code_out = code0
            x, y = x0, y0
        else:
            code_out = code01
            x, y = x1, y1
        
        # compute intersection
        if code_out & TOP:
            yc = WT
            xc = x + (x1 - x0) * (WT - y) / (y1 - y0)
        elif code_out & BOTTOM:
            # y = WB
            yc = WB
            xc = x + (x1 - x0) * (WB - y) / (y1 - y0)
        elif code_out & RIGHT:
            # x = WR
            xc = WR
            yc = y + (y1 - y0) * (WR - x) / (x1 - x0)
        elif code_out & LEFT:
            # x = WL
            xc = WL
            yc = y + (y1 - y0) * (WL - x) / (x1 - x0)

        if code_out == code0:
            x0, y0 = xc, yc
            code0 = compute_code(x0, y0, WL, WR, WB, WT)
        else:
            x1, y1 = xc, yc
            code1 = compute_code(x1, y1, WL, WR, WB, WT)

if __name__=="__main__":
    WL, WR = 10, 30   # left, right boundary
    WB, WT = 10, 20   # bottom, top boundary

    # test line
    x0, y0 = 0, 15
    x1, y1 = 40, 25

    ok, result = cohen_sutherland_clip(x0, y0, x1, y1, WL, WR, WB, WT)
    if ok:
        print("Clipped line:", result)
    else:
        print("Line rejected")
