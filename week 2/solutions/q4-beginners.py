def rotateLeft(d, arr):
    new_array = [0] * len(arr)
    
    for index in range(0, len(arr)):
        # for example, -1 % 10 = 9 since -1*10 + 9 = -1
        # the remainder always has to be positive
        new_index = (index - d) % len(arr)
        new_array[new_index] = arr[index]
        
    return new_array

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    print(rotateLeft(d, arr))