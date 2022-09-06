from code import Utils
import math
import random

class Num:
    def __init__(self, c, s):
        self.n = 0                  # items seen
        self.at = c if c else 0     # column  position
        self.name = s or ""         # column name
        self._has = []          # kept data
        self.lo = float('inf')           # lowest seen
        self.hi = -float('inf')          # highest seen
        self.isSorted = True # no updates since last sort of data

    def nums(self):
        return self._has

    def add(self, v):
        if v != "?":
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
    
    def div(self,a):
        a = self.nums()
        return (Utils.per(a,0.9) - Utils.per(a,0.1)) / 2.58

    def mid(self):
        return Utils.per(self.nums(),0.5)

