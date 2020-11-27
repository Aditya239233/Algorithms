'''
    Given an array, and the target sum to find, we find three distinct elements where the sum of 
    three elements is equal to the target sum. Find all possible combinations.
'''

def threeSum(array: list, target: int) -> list:
    array.sort()
    triplets = []
    
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == target:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
    return triplets

if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    result = threeSum(array, target)
    print(result)