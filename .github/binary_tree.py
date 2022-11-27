from node import Node

COUNT = [10]

class BinaryTree:

  def __init__(self, data=None):
    self.root = None

  # ==================== ADICIONAR ===============================
  
  def adicionar(self, value):
    node = Node(value)
    no = None
    indice = self.root
    while (indice):
      no = indice
      if value < indice.data:
        indice = indice.left
      elif value == indice.data:
        return print("O valor " + str(value) + " ja está inserido na árvore")
      else:
        indice = indice.right
    if no is None:
      self.root = node
    elif value < no.data:
      no.left = node
    else:
      no.right = node

  # ================== BUSCA ==================

  def search(self, value):
    return self._search(value, self.root)

  def _search(self, value, node):
    if node is None:
      return print("O valor " + str(value) + " não está na árvore")
    if node.data == value:
      return print("O valor " + str(value) + " está na árvore")
    if value < node.data:
      return self._search(value, node.left)
    else:
      return self._search(value, node.right)

  # =================== REMOVER ===================

  def remove(self, value):
     print("O valor " + str(value) + " foi removido")
     return self._remove(value, self.root)

  def _remove(self, value, node):
    if value < node.data:
      node.left = self._remove(value, node.left)
    elif value > node.data:
      node.right = self._remove(value, node.right)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      else:
        def _menorFolha(node=None):
          while node.left:
            node = node.left
          return node.data
        organize = _menorFolha(node.right)
        node.data = organize
        node.right = self._remove(organize, node.right)
    return node

  # ======================= IMPRESSÃO ESTRUTURA DA ÁRVORE GRAFICO ========================================
  
  def height(self,root):
    if root is None:
        return 0
    return max(self.height(root.left), self.height(root.right))+1
 
 
  def getcol(self,h):
      if h == 1:
          return 1
      return self.getcol(h-1) + self.getcol(h-1) + 1
   
   
  def printTree(self,M, root, col, row, height):
      if root is None:
          return
      M[row][col] = root.data
      self.printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
      self.printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
   
   
  def TreePrinter(self):
      h = self.height(self.root)
      col = self.getcol(h)
      M = [[0 for _ in range(col)] for __ in range(h)]
      self.printTree(M, self.root, col//2, 0, h)
      for i in M:
          for j in i:
              if j == 0:
                  print(".", end=" ")
              else:
                  print(j, end=" ")
          print("")

  # ============================================================================================