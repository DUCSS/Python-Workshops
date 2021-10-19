"""
for index in range(lower_bound, upper_bound, step):
		statements

range(lower_bound, upper_bound, step) returns an array which starts with
lower_bound and where each of the next elements is greater than the previous one by step.
The last element has to be smaller than upper_bound.

if step is not specified then step will be equal to 1
"""

def for_loop_example():

    print(f"range(1, 10): {list(range(1, 10))}")
    print(f"range(1, 19, 2): {list(range(1, 19, 2))}")
    print(f"range(1, 20, 2): {list(range(1, 20, 2))}")

    # printing elements (and their indicies) of an array that are greater than 10

    array = [0, 10, 11, -1, 100, 228, 5, 70]

    # NB index will not be visible outside for loop, since it is declared inside it
    for index in range(0, len(array)):
        if array[index] > 10:
            print(f"Element at index {index} is greater than 10 {array[index]}")

    # however range is normally used when we need to know indicies if we just need 
    # to process the elements we can directly do:

    # NB element will not be visible outside for loop since it is declared inside it
    for element in array:
        if element > 10:
            print(f"This element is greater than 10: {element}")


    # When we go through the array (iterate over) without using the indicies for
    # loop is commonly referred to as "foreach"


if __name__ == "__main__":
    for_loop_example()