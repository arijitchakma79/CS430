"""
    FROM HW1
"""

class CohenSutherland:
    INSIDE = 0  # 0000
    LEFT   = 1  # 0001
    RIGHT  = 2  # 0010
    BOTTOM = 4  # 0100
    TOP    = 8  # 1000

    def __init__(self, x_min, y_min, x_max, y_max):
        self.xmin = x_min
        self.ymin = y_min
        self.xmax = x_max
        self.ymax = y_max

    def compute_out_code(self, x, y):
        code = CohenSutherland.INSIDE

        if x < self.xmin:
            code |= CohenSutherland.LEFT
        elif x > self.xmax:
            code |= CohenSutherland.RIGHT

        if y < self.ymin:
            code |= CohenSutherland.BOTTOM
        elif y > self.ymax:
            code |= CohenSutherland.TOP

        return code

    def clip_line(self, x1, y1, x2, y2):
        code1 = self.compute_out_code(x1, y1)
        code2 = self.compute_out_code(x2, y2)

        while True:
            if not (code1 | code2):
                return (x1, y1, x2, y2)

            elif code1 & code2:
                return None
            else:
                code_out = code1 if code1 else code2  

                if code_out & CohenSutherland.TOP:
                    if y2 == y1:  # Horizontal line
                        x = x1 if code1 & CohenSutherland.TOP else x2
                    else:
                        x = x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1)
                    y = self.ymax
                elif code_out & CohenSutherland.BOTTOM:
                    if y2 == y1:  # Horizontal line
                        x = x1 if code1 & CohenSutherland.BOTTOM else x2
                    else:
                        x = x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1)
                    y = self.ymin
                elif code_out & CohenSutherland.RIGHT:
                    if x2 == x1:  # Vertical line
                        y = y1 if code1 & CohenSutherland.RIGHT else y2
                    else:
                        y = y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1)
                    x = self.xmax
                elif code_out & CohenSutherland.LEFT:
                    if x2 == x1:  # Vertical line
                        y = y1 if code1 & CohenSutherland.LEFT else y2
                    else:
                        y = y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1)
                    x = self.xmin

                if code_out == code1:
                    x1, y1 = x, y
                    code1 = self.compute_out_code(x1, y1)
                else:
                    x2, y2 = x, y
                    code2 = self.compute_out_code(x2, y2)
        
if __name__ == "__main__":
    clipper = CohenSutherland(0, 0, 100, 100)
    print(clipper.clip_line(-20, 50, 120, 150))  
    print(clipper.clip_line(10, 10, 90, 90))     
    print(clipper.clip_line(-10, -10, -5, -5))