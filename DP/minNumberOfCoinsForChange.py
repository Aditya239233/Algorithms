'''
    Given the target amount of money and an array containing all denominators, 
    return the least number of coins used to form change for target amount.
'''

def minNumOfCoinsForChange(n: int, denoms: list) -> int:
    numOfCoins = [float("inf") for _ in range(n+1)]
    numOfCoins[0] = 0

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
    return numOfCoins[-1] if numOfCoins[-1] != float("inf") else -1

if __name__ == "__main__":
    n = 10
    denoms = [1, 5, 10, 25]
    result = minNumOfCoinsForChange(n, denoms)
    print(result)