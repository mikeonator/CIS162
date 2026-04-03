# Week 1 - CIS162 - Git Functions Project - mike's half
from Ian_Sarlotti import rect_area


def rect_solid_area(x, y, z):
    return 2*(rect_area(x, y) + rect_area(x, z) + rect_area(y, z))
