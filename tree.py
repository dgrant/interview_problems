#!/usr/bin/env python3

import random
from collections import deque

id = 1
prob1 = 0
prob2 = 2
n = 4

class TreeNode:
    def __init__(self):
        global id
        self.left = None
        self.right = None
        self.id = id
        id += 1

    def __str__(self):
        print("id -> {0}, {1}".format(self.left.id, self.right.id))


def add_children(node):
    nodes = []
    node.left = TreeNode()
    nodes.append(node.left)
    node.right = TreeNode()
    nodes.append(node.right)
    return nodes

def add_children_randomly(node):
    nodes = []
#    if random.random() > prob1:
    node.left = TreeNode()
    nodes.append(node.left)
#        if random.random() > prob2:
#            node.right = TreeNode()
#            nodes.append(node.right)
#    if random.random() > prob1:
    node.right = TreeNode()
    nodes.append(node.right)
#        if random.random() > prob2:
#            node.left = TreeNode()
#            nodes.append(node.left)
    return nodes

def create_tree():
    t = TreeNode() 
    new_nodes = [t]
    for i in range(1, n):
        nodes = new_nodes
        print("level", i+1, ":")
        new_nodes = []
        for node in nodes:
            print("parent:", node.id)
            new_children = add_children_randomly(node)
            new_nodes += new_children
            for nn in new_children:
                print(nn.id)
    return t


def dfs(tree):
    yield tree
    if tree.left != None:
        yield from dfs(tree.left)
    if tree.right != None:
        yield from dfs(tree.right)

def bfs(tree):
    q = deque()
    q.append(tree)
    while len(q) > 0:
        n = q.popleft()
        yield n
        if n.left != None:
            q.append(n.left)
        if n.right != None:
            q.append(n.right)


if __name__ == '__main__':
    print("creating...")
    t = create_tree()
    print("traversing dfs...")
    for node in dfs(t):
        print(node.id)

    print("traversing bfs...")
    for node in bfs(t):
        print(node.id)
