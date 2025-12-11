import numpy as np
import sys

def build_vrc_transform(VRP, VPN, VUP):
    print("[DEBUG inside transform_vrc]", "VRP=", VRP, "VPN=", VPN, "VUP=", VUP, file=sys.stderr)
    VRP = np.array(VRP, float)
    VPN = np.array(VPN, float)
    VUP = np.array(VUP, float)
    print("[DEBUG inside transform_vrc] After conversion:", "VRP=", VRP, "VPN=", VPN, "VUP=", VUP, file=sys.stderr)

    # n-axis points INTO THE SCENE (viewer looks along +z)
    # For HW5 conventions, DO NOT flip VPN.
    n_hat = VPN / np.linalg.norm(VPN)

    # project VUP into plane perpendicular to n
    vup_proj = VUP - np.dot(VUP, n_hat) * n_hat

    if np.linalg.norm(vup_proj) < 1e-8:
        if abs(n_hat[2]) < 0.9:
            vup_proj = np.array([0, 0, 1], float)
        else:
            vup_proj = np.array([0, 1, 0], float)
        vup_proj = vup_proj - np.dot(vup_proj, n_hat) * n_hat

    vup_proj /= np.linalg.norm(vup_proj)

    # u = vup × n
    u_hat = np.cross(vup_proj, n_hat)
    u_hat /= np.linalg.norm(u_hat)

    # v = n × u
    v_hat = np.cross(n_hat, u_hat)
    v_hat /= np.linalg.norm(v_hat)

    u_trans = -np.dot(u_hat, VRP)
    v_trans = -np.dot(v_hat, VRP)
    n_trans = -np.dot(n_hat, VRP)
    
    print("[DEBUG inside transform_vrc] u_hat=", u_hat, "v_hat=", v_hat, "n_hat=", n_hat, file=sys.stderr)
    print("[DEBUG inside transform_vrc] Translation terms: u_trans=", u_trans, "v_trans=", v_trans, "n_trans=", n_trans, file=sys.stderr)

    M = np.array([
        [u_hat[0], u_hat[1], u_hat[2], u_trans],
        [v_hat[0], v_hat[1], v_hat[2], v_trans],
        [n_hat[0], n_hat[1], n_hat[2], n_trans],
        [0,        0,        0,        1]
    ])
    
    print("[DEBUG inside transform_vrc] Final matrix M:", file=sys.stderr)
    print(M, file=sys.stderr)

    return M
