
#    4
#  2   6
# 1 3 5 7

class Node:
    def __init__(self, left, data, right):
        self.left = left
        self.right = right
        self.data = data

root = Node(Node(Node(None, 1, None), 2, Node(None, 3, None)), 4, Node(Node(None, 5, None), 6, Node(None, 7, None)))


def contains_sum(root, k):
    return contains_sum_(root, k, [root.data])    

def contains_sum_(node, k, parents):
    for parent in parents:
        if parent + node.data == k:
            return True
    parents.append(node.data)
    return node.left != None and contains_sum_(node.left, k, parents) or \
        node.right != None and contains_sum_(node.right, k, parents)
        
for i in range(1, 20):
    print i, contains_sum(root, i)
