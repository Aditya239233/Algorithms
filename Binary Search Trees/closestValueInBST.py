'''
    Given a BST and a target value, find the closest int value to the target in the tree
'''

from .construction import BST

def findClosestValueInBST(tree: BST, target: int) -> int:
    closest = float("inf")
    currentNode = tree
    while currentNode is not None:
        if abs(target - currentNode.value) < closest:
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif currentNode > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest