from Cols import Cols
from Row import Row
from Utils import parse_csv

class Data:
    def __init__(self, src, nums, separator):
        self.cols = None
        self.rows = []
        self.n = nums
        def func(row):
            nonlocal self
            self.add(row)
        if isinstance(src, str):
            parse_csv(src, func, separator)
        else:
            for row in (src or []):
                self.add(row)
    
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            if hasattr(xs,'cells'):
                self.rows.append(xs)
            else:
                self.rows.append(Row(xs))
            row = self.rows[-1]
            for todo in (self.cols.x, self.cols.y):
                for col in todo:
                    col.add(row.cells[col.at], self.n)

    def stats(self, places, show_cols="data.cols.x", todo):
        show_cols = show_cols or self.cols.y
        todo = todo or "mid"
        
        t= {}
        for col in show_cols:
            if fun == 'mid':
                temp = col.mid()
            else:
                temp = fun(col)
            if isinstance(temp, float):
                temp = round(temp, places)
            t[col.name] = temp
        return t
