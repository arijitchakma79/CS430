from depth_cue import depth_cue

def z_buffer_update(x, y, z_npc, zbuffer, framebuffer, base_color, F, B):
    if y < 0 or y >= len(zbuffer) or x < 0 or x >= len(zbuffer[0]):
        return

    if z_npc < 0 or z_npc > 1:
        return

    if z_npc >= zbuffer[y][x]:
        return

    zbuffer[y][x] = z_npc

    z_vrc = F + z_npc * (B - F)

    shaded_color = depth_cue(base_color, z_vrc, F, B)

    framebuffer[y][x] = shaded_color
