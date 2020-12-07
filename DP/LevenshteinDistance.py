'''
    Given two strings, return the minimum number of edits 
    required for the first string to be transformed into the second string
'''

def levenshteinDistance(stringOne: str, stringTwo: str) -> int:
    edits = [[x for x in range(len(stringOne) + 1)] for y in range(len(stringTwo) + 1)]
    for i in range(1, len(stringTwo) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    
    for i in range(1, len(stringTwo) + 1):
        for j in range(1, len(stringOne) +1):
            if stringTwo[i - 1] == stringOne[j - 1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1]) + 1
    return edits[-1][-1]

if __name__ == "__main__":
    stringOne = "abc"
    stringTwo = "yabd"
    result = levenshteinDistance(stringOne, stringTwo)
    print(result)