import math

class Transform:
    def __init__(self):
        self.matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

    def multiply(self, M):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += M[i][k] * self.matrix[k][j]
        self.matrix = result

    def translate(self, dx, dy):
        T = [
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ]
        self.multiply(T)

    def scale(self, sx, sy):
        S = [
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ]
        self.multiply(S)

    def rotate(self, theta_deg):
        theta = math.radians(theta_deg)
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        R = [
            [cos_t, -sin_t, 0],
            [sin_t,  cos_t, 0],
            [0, 0, 1]
        ]
        self.multiply(R)

    def apply(self, x, y):
        x_new = self.matrix[0][0]*x + self.matrix[0][1]*y + self.matrix[0][2]
        y_new = self.matrix[1][0]*x + self.matrix[1][1]*y + self.matrix[1][2]
        return x_new, y_new