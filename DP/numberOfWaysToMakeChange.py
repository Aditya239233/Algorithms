'''
    Given the target amount of money and an array containing all denominators, 
    return the total number of ways we can make change to get to the target amount
'''

def numberOfWaysToMakeChange(n: int, denoms: list) -> int:
    ways = [0 for _ in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, 1+n):
            if denom <=amount:
                ways[amount] += ways[amount - denom]
    return ways[n]

if __name__ == "__main__":
    n = 10
    denoms = [1, 5, 10, 25]
    result = numberOfWaysToMakeChange(n, denoms)
    print(result)
