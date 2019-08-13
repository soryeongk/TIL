from BreathFirstTraversal import *


root = Node('A')
nb = Node('B')
nc = Node('C')
nd = Node('D')
ne = Node('E')
nf = Node('F')
ng = Node('G')
nh = Node('H')
nj = Node('J')

root.left = nb
root.right = nc
nb.left = nd
nb.right = ne
nc.left = nf
nc.right = ng
nd.left = nh
nf.right = nj

bt = BinaryTree(root)

def test_bft():
    assert ['A','B','C','D','E','F','G','H','J'] ==  bt.bft()
