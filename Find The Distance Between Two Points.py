#Find The Distance Between Two Points
#AB = √(xb - xa)2 + (yb - ya)2

def distance(x1, y1, x2, y2):
    from math import sqrt
    dis_ab = round((sqrt(((x2 - x1)**2) + (y2 - y1)**2)),2)
    return dis_ab


print(distance(1, 1, 0, 0))