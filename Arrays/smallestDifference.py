'''
    Given 2 arrays, find pairs for numbers from each array such that the difference is minimized
'''

def smallestDifference(arrayOne: list, arrayTwo: list) -> list:

    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        
        if current < smallest:
            smallestPair = [firstNum, secondNum]
            smallest = current

    return smallestPair


    
if __name__ == "__main__":
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 138, 135, 15, 17]
    result = smallestDifference(arrayOne, arrayTwo)
    print(result)