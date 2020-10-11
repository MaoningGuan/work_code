#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A:10|E:2,3
A,B,30
A,E,10
B,C,50
B,D,30
E,F,3
E,K,2
F,G,30
F,H,0
H,I,IP
K,M,30
K,N,50
"""
import collections
# A,B,30,E,10,C,50,D,30,F,3,K,2,G,30,H,0,I,IP,M,30,N,50

class TreeNode:
    def __init__(self, x, a=None, b=None):
        self.val = x
        self.left_val = a
        self.right_val = b
        self.left = None
        self.right = None


def deserialize(nodes):
    if not nodes:
        return
    nodes = collections.deque(nodes)
    queue = collections.deque([nodes[0]])
    # # A,B,30,E,10,C,50,D,30,F,3,K,2,G,30,H,0,I,IP,M,30,N,50
    n = len(nodes)
    head = root
    root = TreeNode(nodes.popleft())
    while nodes:
        node = nodes.popleft()
        root.left = node
        node = nodes.popleft()
        root.left_val = node
        node = nodes.popleft()
        root.right = node
        node = nodes.popleft()
        root.right_val = node

        root = root.left







