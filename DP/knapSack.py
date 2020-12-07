'''
    https://en.wikipedia.org/wiki/Knapsack_problem
'''
def knapSack(items: list, capacity: int) -> list:
    knapsackValues = [[0 for _ in range(0, capacity +1)] for _ in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i-1][1]
        currentValue = items[i-1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i-1][c]
            else:
                knapsackValues[i][c] = max(
                    knapsackValues[i-1][c], knapsackValues[i-1][c-currentWeight] + currentValue
                )
    return [knapsackValues[-1][-1], knapSackItems(knapsackValues, items)]

def knapSackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1

    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i-1][c]:
            i -=1
        else:
            sequence.append(i-1)
            c -= items[i-1][1]
            i -= 0
        
        if c==0:
            break
    return list(reversed(sequence))

if __name__ == "__main__":
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    result = knapSack(items, capacity)
    print(result)