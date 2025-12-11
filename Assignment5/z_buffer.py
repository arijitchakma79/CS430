from depth_cue import depth_cue

def z_buffer_update(x, y, z_npc, zbuffer, framebuffer, base_color, F, B):

    # --------------------------------------------------------
    # BOUNDS CHECK
    # --------------------------------------------------------
    if y < 0 or y >= len(zbuffer) or x < 0 or x >= len(zbuffer[0]):
        return

    # --------------------------------------------------------
    # CLIP IN NPC DEPTH SPACE: 0 = near, 1 = far
    # --------------------------------------------------------
    if z_npc < 0 or z_npc > 1:
        return

    # --------------------------------------------------------
    # DEPTH TEST: smaller z is closer
    # --------------------------------------------------------
    if z_npc >= zbuffer[y][x]:
        return  # farther → reject

    # Update zbuffer
    zbuffer[y][x] = z_npc

    # --------------------------------------------------------
    # Convert NPC → VRC z before depth cueing
    #
    # NPC z formula: z_npc = (F - z_vrc) / (F - B)
    #
    # Solve:
    # z_vrc = F - z_npc * (F - B)
    # --------------------------------------------------------
    z_vrc = F - z_npc * (F - B)

    # Compute depth-cued color
    shaded_color = depth_cue(base_color, z_vrc, F, B)

    framebuffer[y][x] = shaded_color
