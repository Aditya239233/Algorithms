'''
    You are initially position at the 0th index of the array. Each element in the array represents 
    your maximum jump length from that position. Determine whether you will be able to reach the last index (-1)
'''

def jumpGame(array: list) -> bool:
    if len(array) == 1:
            return True
        
    size = len(array)
    max_jump = array[0]
    for i in range(size):
        if max_jump <= i  and array[i] == 0:
            return False

        if i + array[i] >= max_jump:
            max_jump = i + array[i]

        if max_jump >= size - 1:
            return True
    return False

if __name__ == "__main__":
    array = [3,2,1,0,4]
    result = jumpGame(array)
    print(result)