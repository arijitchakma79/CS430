def project_vertices(vertices_vrc, PRP, parallel, F):
    PRPx, PRPy, PRPz = PRP
    eps = 1e-9

    vertices_proj = []

    for (u, v, n) in vertices_vrc:

        if parallel:
            xprime = u
            yprime = v
            zprime = n

        else:
            denom = (n - PRPz)
            if abs(denom) < eps:
                xprime = u
                yprime = v
                zprime = n
            else:
                lam = (F - PRPz) / denom
                xprime = PRPx + lam * (u - PRPx)
                yprime = PRPy + lam * (v - PRPy)
                zprime = n

        vertices_proj.append((xprime, yprime, zprime))

    return vertices_proj
