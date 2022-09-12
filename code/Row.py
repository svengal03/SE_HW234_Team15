from Utils import copy

class Row:
  def __init__(self, t, data):
    self.cells = t
    self.cooked = copy(t)
    self.isEvaled = False
    self.outerSpace= data

    return self.cells, self.cooked, self.isEvaled, self.outerSpace
