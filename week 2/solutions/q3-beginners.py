if __name__ == '__main__':

    n = int(input())
    # don't worry about next two lines we can assume we are given an array without having
    # to read from the input
    arr = map(int, input().split())
    arr = list(arr)
    
    maximum = arr[0]
    
    for element in arr:
        if element > maximum:
            maximum = element
            
        
    # since elements of the array lie in [-100, 100] by the problem statement
    # we have to set the runner_up to the smallest possible value - 1
    # so that we can correctly process the data
    # if we set it to 0, for example, we may end up having an input of all negative
    # numbers which will make us output zero since no negative number is greater than
    # zero, this is going to be wrong.
    runner_up = -101
    
    for element in arr:
        if element != maximum and element > runner_up:
            runner_up = element
   
    print(runner_up)