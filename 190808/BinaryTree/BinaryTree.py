class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l,r) + 1

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = [self.data]
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r
    
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
    
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
    
    def inorder(self):
        if self.root:
            return self.root.inorder()
        return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        return []
