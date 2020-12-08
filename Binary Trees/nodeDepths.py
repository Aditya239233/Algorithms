'''
    Node depth is the distance between a node in a Binary tree and the tree's root.
    Given a Binary Tree, return the sum of its nodes depths
'''
from .construction import BinaryTree

def nodeDepths(root: BinaryTree, depth: int = 0) -> int:
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)