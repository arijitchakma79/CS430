def depth_cue(base_color, z_vrc, F, B):
    R0, G0, B0 = base_color

    t = (z_vrc - B) / (F - B)

    if t < 0:
        t = 0
    if t > 1:
        t = 1

    R = int(R0 * t)
    G = int(G0 * t)
    Bc = int(B0 * t)

    return (R, G, Bc)