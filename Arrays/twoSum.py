'''
    Given an array, and the target sum to find, we find two distinct elements where the sum of 
    two elements is equal to the target sum.
'''
def twoSum(array: list, target: int) -> list:

    for val in array:
        if (target - val) in array and array.index(val) != array.index(target - val):
            return [val, target - val]
    return []


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    result = twoSum(array, target)
    print(result)