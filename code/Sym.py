import math

class Sym():
    def __init__(self, c_name="", c_position=0):
        self.n = 0
        self.at = c_position
        self.name = c_name
        self._has = dict()

    def add(self, k):
        if k != "?":
            self.n += 1
            self._has[k] = self._has.get(k, 0) + 1

    def mid(self):
        mode = max(self._has, key=self._has.get)
        return mode

    def div(self):
        e = 0

        def func(p):
            return p * math.log(p, 2)

        for v in self._has.values():
            if v > 0:
                e = e - func(v / self.n)
        return e


if __name__ == '__main__':
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
