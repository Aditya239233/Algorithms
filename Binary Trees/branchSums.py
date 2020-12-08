'''
    Given a Binary Tree, return the sum of all the branches in the Binary Tree.
'''

from .construction import BinaryTree

def branchSums(root: BinaryTree) -> list:
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node: BinaryTree, runningSum: int, sums: list):
    if node is None:
        return
    
    newRunningSums = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSums)
        return
    
    calculateBranchSums(node.left, newRunningSums,sums)
    calculateBranchSums(node.right, newRunningSums,sums)