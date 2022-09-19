from code import Utils

class Row:
  def __init__(self, t, data=None):
    self.cells = t
    self.cooked = Utils.copy(t)
    self.isEvaled = False
    self.outerSpace= data

    return self.cells, self.cooked, self.isEvaled, self.outerSpace
