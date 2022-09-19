from code import Cols
from code import Row
from code import Utils

class Data:
    def __init__(self, src, nums=None, separator=None):
        self.cols = None
        self.rows = []
        self.n = nums
        def func(row):
            nonlocal self
            self.add(row)
        if isinstance(src, str):
            Utils.parse_csv(src, self.add)
        else:
            for row in (src or []):
                self.add(row)
    
    def add(self, xs: Row):
        if not self.cols:
            self.cols = Cols.Cols(xs)
        else:
            row = xs if type(xs) == Row else Row.Row(xs)
            self.rows.append(row)
            for col in self.cols.x + self.cols.y:
                    col.add(row.cells[col.at])

    def stats(self, places=2, show_cols=None, todo=None):
        show_cols = show_cols or self.cols.y
        todo = todo or self.cols.mid
        
        t= {}
        for col in show_cols:
            '''if todo == 'mid':
                temp = col.mid()
            else:
                temp = col.div()'''
            temp = todo(col) 
            if isinstance(temp, float):
                temp = round(temp, places)
            t[col.name] = temp
        return t
