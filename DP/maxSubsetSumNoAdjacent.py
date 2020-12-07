'''
    Given an array of positive numbers, return the maximum sum of non-adjacent 
    elements in the array
'''

def maxSubsetSumNoAdjacent(array: list) -> int:
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second, first = first, current
    return first

if __name__ == "__main__":
    array = [10, 20, 70, 45]
    result = maxSubsetSumNoAdjacent(array)
    print(result)