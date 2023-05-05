class Node:

  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left

  def __str__(self):
    return str(self.data)


