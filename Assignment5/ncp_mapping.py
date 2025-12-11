def npc_mapping(vertices_proj, umin, umax, vmin, vmax, F, B):

    vertices_npc = []

    for (x_proj, y_proj, z_vrc) in vertices_proj:

        x_npc = 2 * (x_proj - umin) / (umax - umin) - 1
        y_npc = 2 * (y_proj - vmin) / (vmax - vmin) - 1

        # Correct near/far mapping: 0 at near, 1 at far
        z_npc = (F - z_vrc) / (F - B)

        vertices_npc.append((x_npc, y_npc, z_npc))

    return vertices_npc
