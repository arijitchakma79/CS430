class SutherlandHodgman:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def inside(self, p, edge):
        x, y = p
        if edge == "LEFT":
            return x >= self.xmin
        elif edge == "RIGHT":
            return x <= self.xmax
        elif edge == "BOTTOM":
            return y >= self.ymin
        elif edge == "TOP":
            return y <= self.ymax
        return False

    def intersect(self, p1, p2, edge):
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 and y1 == y2:
            return (x1, y1)  

        if edge == "LEFT":
            x = self.xmin
            y = y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1)
        elif edge == "RIGHT":
            x = self.xmax
            y = y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1)
        elif edge == "BOTTOM":
            y = self.ymin
            x = x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1)
        elif edge == "TOP":
            y = self.ymax
            x = x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1)
        return (x, y)

    def clip_edge(self, vertices, edge):
        if not vertices:
            return []

        clipped = []
        prev = vertices[-1]

        for curr in vertices:
            if self.inside(curr, edge):
                if self.inside(prev, edge):
                    clipped.append(curr)
                else:
                    inter = self.intersect(prev, curr, edge)
                    clipped.append(inter)
                    clipped.append(curr)
            else:
                if self.inside(prev, edge):
                    inter = self.intersect(prev, curr, edge)
                    clipped.append(inter)
            prev = curr

        return clipped

    def clip(self, vertices):
        output = vertices
        for edge in ["LEFT", "RIGHT", "BOTTOM", "TOP"]:
            output = self.clip_edge(output, edge)
        return output

if __name__ == "__main__":
    polygon = [(300,150), (450,150), (450,499), (300,499), (300,150)]
    clipper = SutherlandHodgman(100, 100, 400, 400)

    clipped = clipper.clip(polygon)
    print("Clipped Polygon:", clipped)