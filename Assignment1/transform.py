import numpy as np
import math

class Transform:
    def __init__(self):
        self.matrix = np.identity(3, dtype=float)

    def translate(self, dx, dy):
        T = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ], dtype=float)
        self.matrix = T @ self.matrix

    def scale(self, sx, sy):
        S = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ], dtype=float)
        self.matrix = S @ self.matrix

    def rotate(self, theta_deg):
        theta = math.radians(theta_deg)
        R = np.array([
            [math.cos(theta), -math.sin(theta), 0],
            [math.sin(theta),  math.cos(theta), 0],
            [0, 0, 1]
        ], dtype=float)
        self.matrix = R @ self.matrix

    def apply(self, x, y):
        v = np.array([x, y, 1], dtype=float)
        res = self.matrix @ v
        return res[0], res[1]
