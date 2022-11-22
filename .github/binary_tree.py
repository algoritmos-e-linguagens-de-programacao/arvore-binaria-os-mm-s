from node import Node

class BinaryTree:

  def __init__(self):
    self.root = None

  def adicionar(self, value):
    node = Node(value)
    if self.root == None:
      self.root = node
    else:
      if (self.root.value < self.root):
        if (self.root.esquerda == None):
          self.root.esquerda == node
        else:
          if (self.root.esquerda and self.root.direita == None):
            self.root.esquerda = node
          else:
            self.root.esquerda.adicionar(value)
      else:
        if self.root.direita == None:
          self.root.direita == node
        else:
          if (self.root.esquerda and self.root.direita == None):
            self.root.direita = node
          else:
            self.root.direita.adicionar(value)

  def remover():
    return

  def show(self):
    if self.root.esquerda:
      self.root.esquerda.show()
    print(self.root.value),
    if self.root.direita:
      self.root.direita.show()