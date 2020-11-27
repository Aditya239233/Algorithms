'''
    Given two non empty array of integers, determine whether the second array is a 
    subsequence of the first array
'''
def validateSubsequence(array: list, sequence: list) -> bool:
    seqId = 0
    for num in array:
        if num == sequence[seqId]:
            seqId += 1
        if seqId == len(sequence):
            return True
    return False
        

if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    result = validateSubsequence(array, sequence)
    print(result)