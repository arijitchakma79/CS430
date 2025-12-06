import numpy as np
import sys
import math

class Project3D_to_2D:
    def __init__(self, cfg):
        self.VRP = np.array([cfg["X"], cfg["Y"], cfg["Z"]], float)
        self.PRP = np.array([cfg["x"], cfg["y"], cfg["z"]], float)
        self.VPN = np.array([cfg["q"], cfg["r"], cfg["w"]], float)
        self.VUP = np.array([cfg["Q"], cfg["R"], cfg["W"]], float)

        self.umin = cfg["u"]
        self.vmin = cfg["v"]
        self.umax = cfg["U"]
        self.vmax = cfg["V"]

        self.F = cfg["F"]
        self.B = cfg["B"]

        self.width = cfg["o"]
        self.height = cfg["p"]
        self.parallel = cfg["P"]

        self.Mvrc = self.build_vrc_transform()
        self.build_shear_scale()

    def build_vrc_transform(self):
        VRP = self.VRP
        VPN = self.VPN / np.linalg.norm(self.VPN)
        vup_proj = self.VUP - np.dot(self.VUP, VPN) * VPN
        vup_proj /= np.linalg.norm(vup_proj)

        u = np.cross(vup_proj, VPN)
        u /= np.linalg.norm(u)
        v = np.cross(VPN, u)

        T = np.array([
            [1,0,0,-VRP[0]],
            [0,1,0,-VRP[1]],
            [0,0,1,-VRP[2]],
            [0,0,0,1]
        ])

        R = np.array([
            [u[0], u[1], u[2], 0],
            [v[0], v[1], v[2], 0],
            [VPN[0], VPN[1], VPN[2], 0],
            [0,0,0,1]
        ])

        return R @ T

    def build_shear_scale(self):
        prp_vrc = (self.Mvrc @ np.array([*self.PRP,1]))[:3]
        zvp = prp_vrc[2]

        u_center = (self.umin + self.umax) / 2
        v_center = (self.vmin + self.vmax) / 2

        self.shx = (prp_vrc[0] - u_center * prp_vrc[2]) / (prp_vrc[2])
        self.shy = (prp_vrc[1] - v_center * prp_vrc[2]) / (prp_vrc[2])

        du = self.umax - self.umin
        dv = self.vmax - self.vmin

        self.sx = 2 / du
        self.sy = 2 / dv
        self.sz = 1 / (self.F - self.B)
        self.zvp = zvp

    def project_vertex(self, v):
        vx, vy, vz = v
        p = np.array([vx, vy, vz, 1.0])

        p = self.Mvrc @ p
        x, y, z, _ = p

        if not self.parallel:
            x -= self.shx * z
            y -= self.shy * z

            if abs(z - self.zvp) < 1e-9:
                return float("nan"), float("nan"), float("nan")

            x = x * ((-self.zvp) / (z - self.zvp))
            y = y * ((-self.zvp) / (z - self.zvp))

        x = self.sx * (x - (self.umin + self.umax) / 2)
        y = self.sy * (y - (self.vmin + self.vmax) / 2)

        if not self.parallel:
            z_npc = (z - self.B) * self.sz
        else:
            z_npc = (z - self.B) * self.sz

        z_npc = max(0.0, min(1.0, z_npc))

        xs = int((x + 1) * 0.5 * (self.width - 1))
        ys = int((1 - (y + 1) * 0.5) * (self.height - 1))

        return xs, ys, z_npc
