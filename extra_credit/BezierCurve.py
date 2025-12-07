class BezierCurve:
    def __init__(self, N):
        self.N = N

    def de_casteljau(self, P0, P1, P2, P3, t):
        # Level 1
        P01 = ((1-t)*P0[0] + t*P1[0], (1-t)*P0[1] + t*P1[1])
        P12 = ((1-t)*P1[0] + t*P2[0], (1-t)*P1[1] + t*P2[1])
        P23 = ((1-t)*P2[0] + t*P3[0], (1-t)*P2[1] + t*P3[1])

        # Level 2
        P012 = ((1-t)*P01[0] + t*P12[0], (1-t)*P01[1] + t*P12[1])
        P123 = ((1-t)*P12[0] + t*P23[0], (1-t)*P12[1] + t*P23[1])

        # Level 3 (final point)
        return ((1-t)*P012[0] + t*P123[0],
                (1-t)*P012[1] + t*P123[1])

    def bezier_to_polyline(self, P0, P1, P2, P3):
        pts = []
        for i in range(self.N + 1):   # use stored N
            t = i / float(self.N)
            pts.append(self.de_casteljau(P0, P1, P2, P3, t))
        return pts
