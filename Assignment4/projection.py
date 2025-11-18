def project_vertices(vertices_vrc, PRPx, PRPy, PRPz, parallel):
    eps = 1e-9
    vertices_2d = [None] * len(vertices_vrc)

    for i in range(1, len(vertices_vrc)):
        u, v, n = vertices_vrc[i]
        if parallel:
            vertices_2d[i] = (u, v)
        else:
            denom = n - PRPz
            if abs(denom) < eps:
                vertices_2d[i] = (u, v)
            else:
                lam = -PRPz / denom
                u2 = PRPx + lam * (u - PRPx)
                v2 = PRPy + lam * (v - PRPy)
                vertices_2d[i] = (u2, v2)

    return vertices_2d
