import numpy as np

def cyrus_beck_clip(P0, P1, polygon):
    # Direction vector of the line
    D = P1 - P0

    # t-range for the clipped segment
    tE = 0.0  # entering parameter
    tL = 1.0  # leaving parameter

    n = len(polygon)

    for i in range(n):
        Vi = polygon[i]
        Vi1 = polygon[(i + 1) % n]

        # Edge Vector
        E = Vi1 - Vi

        # Compute outward normal (rotate E by +90 degrees for CCW polygons)
        # Normal = (Ey, -Ex)
        N = np.array([E[1], -E[0]])

        # Compute numerator and denominator
        numerator = np.dot(N, Vi - P0)
        denominator = np.dot(N, D)

        if denominator == 0:
            # line is parallel to edge
            if numerator < 0:
                # Line is outside this edge => reject
                return False, None, None
            else:
                # Line is parallel and inside, ignore this edge
                continue
        t = numerator / denominator

        if denominator < 0:
            # potential exiting point
            tE = max(tE, t)
        else:
            # potential leaving point
            tL = min(tL, t)

        if tE > tL:
            return False, None, None

    # Compute clipped points
    P_enter = P0 + tE * D
    P_leave = P0 + tL * D

    return True, P_enter, P_leave


if __name__ == "__main__":
    P0 = np.array([0.0, 0.0])
    P1 = np.array([5.0, 3.0])

    # Rectangle defined CCW
    WL, WR, WB, WT = 1, 4, 1, 3
    polygon = [
        np.array([WL, WB]),
        np.array([WR, WB]),
        np.array([WR, WT]),
        np.array([WL, WT])
    ]

    ok, Pe, Pl = cyrus_beck_clip(P0, P1, polygon)

    if ok:
        print("Clipped segment:")
        print("Enter at:", Pe)
        print("Leave at:", Pl)
    else:
        print("Line rejected")