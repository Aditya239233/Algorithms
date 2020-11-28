'''
    Given an array of integers and an integer, move all instances of that integer to the end
    of the array.
'''

def moveElementToEnd(array: list, toMove: int) -> list:
    
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    result = moveElementToEnd(array, toMove)
    print(result)
