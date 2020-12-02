'''
    Given an array, and the target sum to find, we find four distinct elements where the sum of 
    four elements is equal to the target sum.
'''
from itertools import combinations

def fourSum(array: list, target: int) -> list:
    allQuads = combinations(array, 4)
    quadriplets = []
    for quad in allQuads:
        if sum(quad) == target:
            quadriplets.append(quad)
    
    return quadriplets

if __name__ == "__main__":
    array = [7, 6, 4, -1, 1, 2]
    target = 16
    result = fourSum(array, target)
    print(result)