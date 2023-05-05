from binary_tree import BinaryTree

arvore = BinaryTree()

arvore.adicionar(5)

arvore.adicionar(3)
arvore.adicionar(2)
arvore.adicionar(8)
arvore.adicionar(4)
arvore.adicionar(50)

arvore.adicionar(6)
arvore.adicionar(7)
arvore.adicionar(3)

print("")

arvore.search(8)
arvore.TreePrinter()

print("")

arvore.remove(6)
arvore.TreePrinter()

print("")

arvore.preOrdem()

print("")

arvore.emOrdem()

print("")

arvore.posOrdem()