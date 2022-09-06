import math

def per(t,p):
    p = math.floor(((p or .5) * len(t)) + .5)
    return t[math.max(1, min(len(t), p))]
