from binary_tree import BinaryTree

arvore = BinaryTree()

arvore.adicionar(9)

arvore.adicionar(2)
arvore.adicionar(6)
arvore.adicionar(3)

arvore.adicionar(8)
arvore.adicionar(321)
arvore.adicionar(1)
arvore.adicionar(3)

print("")

arvore.search(9)
arvore.TreePrinter()


print("")


arvore.remove(9)
arvore.TreePrinter()

print("")

arvore.remove(6)
arvore.TreePrinter()