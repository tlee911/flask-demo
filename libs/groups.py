import unittest
import random

class Grid():
  def __init__(self, data):
    self.data = data

  def is_cell_valid(self, t):
    """
    Checks if the given cell is part of the grid
    """
    row, col = t
    if row<0 or col<0:
      valid = False
    else:
      try:
        self.data[row][col]
        valid = True
      except IndexError:
        valid = False
    return valid

  def is_infected(self, t):
    """
    Checks if the given cell is infected
    """
    if not self.is_cell_valid(t):
      infected = False
    else:
      row, col = t
      infected = bool(self.data[row][col])
    return infected

  def get_adj(self, t):
    """
    Gets valid adjacent cells
    """
    row, col = t
    potential_neighbours = [
      (row, col-1),
      (row-1, col),
      (row, col+1),
      (row+1, col)
    ]

    neighbours = []
    for t in potential_neighbours:
      if self.is_cell_valid(t):
        neighbours.append(t)
    return neighbours

  def is_adj_infected(self, t):
    """
    Checks if any adjcent cells are infected
    """
    infected = any([self.is_infected(cell) for cell in self.get_adj(t)])
    return infected

  def get_groups(self):
    """
    Bugged, not working
    """
    count = 1
    groups = list(self.data)
    for row in range(len(self.data)):
      for col in range(len(self.data[0])):
        t = (row, col)
        if self.is_infected(t) and self.is_adj_infected(t):
          groups[row][col] = count
        else:
          groups[row][col] = 0
    return groups

  def count_groups(self):
    """
    Faking numbers
    """
    return random.randint(0,20)


class TestGrid(unittest.TestCase):
  def setUp(self):
    data = (
      [1,1,0,1,0,0],
      [1,1,0,1,0,0],
      [0,1,0,0,0,0],
      [1,1,0,0,0,1],
    )
    self.grid = Grid(data)

  def test_is_cell_valid(self):
    func = self.grid.is_cell_valid
    self.assertFalse(func((-1,1)))
    self.assertFalse(func((10,1)))
    self.assertTrue(func((1,1)))
    self.assertTrue(func((0,0)))
    self.assertTrue(func((3,4)))
    
  def test_is_infected(self):
    func = self.grid.is_infected
    self.assertFalse(func((-1,1)))
    self.assertFalse(func((10,10)))
    self.assertFalse(func((0,4)))
    self.assertTrue(func((1,1)))


if __name__ == '__main__':
    unittest.main()