def clip_polyline(polyline, clipper):
    if not polyline or len(polyline) < 2:
        return []
    
    clipped = []
    for i in range(len(polyline) - 1):
        x1, y1 = polyline[i]
        x2, y2 = polyline[i + 1]
        
        result = clipper.clip_line(x1, y1, x2, y2)
        if result:
            cx1, cy1, cx2, cy2 = result
            # Check if we need to add the first point
            # Use a small epsilon for floating point comparison
            if i == 0:
                clipped.append((cx1, cy1))
            elif clipped:
                # Check if the last point is different from the first point of this segment
                last_x, last_y = clipped[-1]
                if abs(last_x - cx1) > 1e-6 or abs(last_y - cy1) > 1e-6:
                    clipped.append((cx1, cy1))
            else:
                clipped.append((cx1, cy1))
            
            # Always add the second point
            clipped.append((cx2, cy2))
    
    return clipped