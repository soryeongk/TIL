'''
traversal = 빈리스트
q = 빈 큐
빈트리가 아니면, root node를 q에 추가 (enqueue)
q가 비어있지 않은 동안은
    node = q에서 원소를 추출
    node를 방문
    node의 왼쪽, 오른쪽 자식(잇으면)들을 q에 추가
q가 빈 큐가 되면 모든 노드 방문 완료
'''

class ArrayQueue:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:
    
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def preorder(self):
        traversal = [self.data]
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

class BinaryTree:
    
    def __init__(self, r):
        self.root = r

    def preorder(self):
        if self.size:
            return self.root.preorder()
        return []

    def bft(self):
        q = ArrayQueue()
        traversal = []
        
        if self.root:
            q.enqueue(self.root)

        while not q.isEmpty():
            node = q.dequeue()
            traversal.append(node.data)

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return traversal
'''
노드를 방문
자신을 먼저 queue에 넣기
좌우 자식이 있는지 확인하고
    자식이 있으면 좌우 순으로 queue에 넣기
queue의 가장 앞 원소의 data를 traversal에 append
'''
