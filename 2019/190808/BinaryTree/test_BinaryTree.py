from BinaryTree import *


alphabets = list('ABCDEFGHJ')


root = Node('A')
nb = Node('B')
nc = Node('C')
nd = Node('D')
ne = Node('E')
nf = Node('F')
ng = Node('G')
nh = Node('H')
nj = Node('J')
nk = Node('K')

root.left = nb
root.right = nc
nb.left = nd
nb.right = ne
nc.left = nf
nc.right = ng
nd.left = nh
nf.right = nj

BiTree = BinaryTree(root)

def test_size():
    assert BiTree.size() == 9

def test_depth():
    assert BiTree.depth() == 4

def test_inorder():
    assert BiTree.inorder() == ['H','D','B','E','A','F','J','C','G']

def test_preorder():
    assert BiTree.preorder() == ['A', 'B', 'D', 'H', 'E', 'C', 'F', 'J', 'G']

def test_postorder():
    assert BiTree.postorder() == ['H', 'D', 'E', 'B', 'J', 'F', 'G', 'C', 'A']
