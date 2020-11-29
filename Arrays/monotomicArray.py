'''
    Given an array of integers, find whether the integers in the array are monotomic or not.
    Monotomic: Strictly increasing or decreasing
'''

def monotomicArray(array: list) -> bool:
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if breakDirection(direction, array[i-1], array[i]):
            return False
    return True 

def breakDirection(direction, previous, current):
    difference = current - previous
    if direction > 0:
        return difference < 0
    return difference > 0

if __name__ == "__main__":
    array = [-1, -5, -10, -1100, -7234, -112345]
    result = monotomicArray(array)
    print(result)