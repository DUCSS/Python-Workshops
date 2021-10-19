def sample_array_operations():

    # simple array creation
    array = [0, 1, 2, 3, 4]
    print(array)

    a = 10 
    b = 7

    # creating array out of variables
    array = [a, 0, b, b]

    print(array)

    # add a new element to the end
    array.append(100)

    print(array)

    # add a number of elements to the end
    array.extend([1000,100000, -28])

    print(array)

    # print the first element of the array
    # NB indexes start at 0 and go up to (array length - 1)
    print(f"First element of the array: {array[0]}")

    # print the length of the array
    print(f"Length of array: {len(array)}")

    # print the last element of the array
    print(f"Last element: {array[-1]}")

    # print the second last element of the array
    print(f"Second last element: {array[-2]}")

    # print second element of the array
    print(f"Second element: {array[1]}")


if __name__ == "__main__":
    sample_array_operations()