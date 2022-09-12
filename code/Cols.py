import re
from code import Sym
from code import Num

# Create
# Columns are created once, then may appear in  multiple slots.

class Cols:
    def __init__(self, names):
        self.names=names  #all column names
        self.all=[]       #all the columns (including the skipped ones)
        self.klass=None   #the single dependent klass column (if it exists)
        self.x=[]         #independent columns (that are not skipped)
        self.y=[]         #depedent columns (that are not skipped)
        
        for c in range(0, len(names)):
            s = names[c] 
            #Numerics start with Uppercase. 
            if re.search("[A-Z]+", s):
                self.all.append(Num.num(c, s))
            else:
                self.all.append(Sym.sym(c, s))
            col = self.all[-1]
            
            # some cols are goal cols
            if s.find(":") == -1:
                if s[-1] == '+' or s[-1] == '-':
                    self.y.append(col) 
                else:
                    self.x.append(col)
                
                if s[-1] == '$':
                    self.klass = col
