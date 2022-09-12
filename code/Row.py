from Utils import copy

class Row:
  def __init__(self, t):
    self.cells = t
    self.cooked = copy(t)
    self.isEvaled = False

    return self.cells, self.cooked, self.isEvaled
