class ViewportMapper:
    def __init__(self, a, b, c, d, j, k, o, p):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.j = j
        self.k = k
        self.o = o
        self.p = p

    def map(self, xw, yw):
        xv = self.j + (xw - self.a) * ((self.o - self.j) / (self.c - self.a))
        yv = self.k + (yw - self.b) * ((self.p - self.k) / (self.d - self.b))
        return xv, yv
