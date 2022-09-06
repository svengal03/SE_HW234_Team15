import math
class Sym:
    def __int__(self,c_name = "" ,c_position = 0):
        self.n = 0 #characters seen
        self.at = c_position # position of column
        self.name = c_name  # name of a column
        self._has = dict() # dictionary to contain freq of a symbol
        
    def add(self,k):
        if k != '?':
            self.n +=1
            if k in self._has:
                self._has[k] +=1
            else:
                self._has[k] =1
    
    def mid(self):
        mode = max(self._has, key = self._has.get)
        return mode
    
    def div(self):
        e=0
        def func(p):
            return  p*math.log(p,2)
        for v in self._has.values():
            if v> 0:
                e = e-func(v/self.n)
        return e
