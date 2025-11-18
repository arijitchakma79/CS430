from vectors import Vector_Operations as V

def world_to_vrc(vertices_world, VRP, VPN, VUP):
    n_hat = V.normalize(VPN)
    u_hat = V.normalize(V.cross(n_hat, VUP))
    v_hat = V.cross(u_hat, n_hat)

    vertices_vrc = [None] * len(vertices_world)
    for i in range(1, len(vertices_world)):
        Pw = vertices_world[i]
        PwT = V.sub(Pw, VRP)
        u = V.dot(u_hat, PwT)
        v = V.dot(v_hat, PwT)
        n = V.dot(n_hat, PwT)
        vertices_vrc[i] = (u, v, n)

    return vertices_vrc
