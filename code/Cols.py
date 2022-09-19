import re
from code import Sym
from code import Num

# Create
# Columns are created once, then may appear in  multiple slots.

class Cols:
    def __init__(self, names):
        self.names=names  # all column names
        self.all=[]       # all the columns (including the skipped ones)
        self.klass=None   # the single dependent klass column (if it exists)
        self.x=[]         # independent columns (that are not skipped)
        self.y=[]         # depedent columns (that are not skipped)
        
        for c in range(0, len(names)):
            s =  re.sub('\n', '' , names[c]) 
            # Numerics start with Uppercase. 
            col = Num.Num(i, s) if re.search(r'^[A-Z]*', s) else Sym.Sym(i, s)
            self.all.append(col)
            
            # some cols are goal cols
            if not s.endswith(':'):
                if  re.search(r'[+!-]', s):
                    self.y.append(col) 
                else:
                    self.x.append(col)
                
                if "!$" in s:
                    self.klass = col
