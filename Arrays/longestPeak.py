'''
    Given an array of integers, find the length of the longest peak in the array
'''

def longestPeak(array: list) -> int:
    longestPeakLength = 0
    i = 0
    while i <= len(array) - 2:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]

        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] <= array[leftIdx + 1]:
            leftIdx -= 1
        
        rightIdx = i + 2
        while rightIdx <= len(array) - 1 and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        
        currentMax = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentMax)
        i = rightIdx
    return longestPeakLength

if __name__ == "__main__":
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    result = longestPeak(array)
    print(result)