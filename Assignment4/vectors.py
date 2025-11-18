import math

class Vector_Operations:
    @staticmethod
    def dot(a, b):
        return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

    @staticmethod
    def cross(a, b):
        return (
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        )

    @staticmethod
    def sub(a, b):
        return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

    @staticmethod
    def normalize(v):
        l2 = Vector_Operations.dot(v, v)
        if l2 == 0.0:
            return (0.0, 0.0, 0.0)
        l = math.sqrt(l2)
        return (v[0]/l, v[1]/l, v[2]/l)
