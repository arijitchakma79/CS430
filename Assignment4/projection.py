def project_vertices(vertices_vrc, PRP, parallel):
    PRPx, PRPy, PRPz = PRP
    eps = 1e-9
    vertices_proj = [None] * len(vertices_vrc)

    for i in range(1, len(vertices_vrc)):
        u, v, n = vertices_vrc[i]

        if parallel:
            xprime = u
            yprime = v
            zprime = n  
        else:
            denom = (n - PRPz)
            if abs(denom) < eps:
                xprime, yprime, zprime = u, v, n
            else:
                lam = -PRPz / denom

                xprime = PRPx + lam * (u - PRPx)
                yprime = PRPy + lam * (v - PRPy)
                zprime = n  
        vertices_proj[i] = (xprime, yprime, zprime)

    return vertices_proj
