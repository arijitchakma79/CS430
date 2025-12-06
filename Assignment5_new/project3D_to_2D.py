import numpy as np


class Project3D_to_2D:
    def __init__(self, cfg):
        self.VRP = np.array([cfg["X"], cfg["Y"], cfg["Z"]], float)
        self.PRP = np.array([cfg["x"], cfg["y"], cfg["z"]], float)
        self.VPN = np.array([cfg["q"], cfg["r"], cfg["w"]], float)
        self.VUP = np.array([cfg["Q"], cfg["R"], cfg["W"]], float)

        self.tx = cfg["j"]
        self.ty = cfg["k"]

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
        self.compute_prp_vrc()
        self.compute_shear_scale()

    def build_vrc_transform(self):
        VRP = self.VRP

        n = -self.VPN
        n = n / np.linalg.norm(n)

        vup_proj = self.VUP - np.dot(self.VUP, n) * n
        vup_proj /= np.linalg.norm(vup_proj)

        u = np.cross(vup_proj, n)
        u /= np.linalg.norm(u)

        v = np.cross(n, u)
        v /= np.linalg.norm(v)

        T = np.array([
            [1,0,0,-VRP[0]],
            [0,1,0,-VRP[1]],
            [0,0,1,-VRP[2]],
            [0,0,0,1]
        ])

        R = np.array([
            [u[0], u[1], u[2], 0],
            [v[0], v[1], v[2], 0],
            [n[0], n[1], n[2], 0],
            [0,   0,   0,   1]
        ])

        return R @ T

    def compute_prp_vrc(self):
        self.PRP_vrc = (self.Mvrc @ np.array([*self.PRP, 1]))[:3]

    def compute_shear_scale(self):
        prp = self.PRP_vrc

        CWu = (self.umin + self.umax) / 2
        CWv = (self.vmin + self.vmax) / 2

        self.shx = (prp[0] - CWu) / prp[2]
        self.shy = (prp[1] - CWv) / prp[2]

        du = self.umax - self.umin
        dv = self.vmax - self.vmin

        self.sx = 2 / du
        self.sy = 2 / dv

        self.sz = 1 / (self.F - self.B)

    def project_vertex(self, v):
        vx = v[0] + self.tx
        vy = v[1] + self.ty
        vz = v[2]

        Pw = np.array([vx, vy, vz, 1.0])

        Pv = self.Mvrc @ Pw
        x, y, z, _ = Pv

        if not self.parallel:
            x -= self.shx * z
            y -= self.shy * z

            prp_z = self.PRP_vrc[2]

            denom = (z - prp_z)
            if abs(denom) < 1e-9:
                denom = -1e-9

            factor = prp_z / denom
            x *= factor
            y *= factor

        CWu = (self.umin + self.umax) / 2
        CWv = (self.vmin + self.vmax) / 2

        x = self.sx * (x - CWu)
        y = self.sy * (y - CWv)

        z_npc = (self.F - z) * self.sz
        z_npc = min(max(z_npc, 0.0), 1.0)

        xs = int((x + 1) * 0.5 * (self.width - 1))
        ys = int((y + 1) * 0.5 * (self.height - 1))

        return xs, ys, z_npc
