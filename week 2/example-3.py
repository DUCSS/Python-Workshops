"""
    Each execution cycle of a loop is called iteration
    “continue” statement makes the loop immediately proceed to the next iteration
    “break” statement makes the loop exit immediately

    continue and break statements are considered a BAD PRACTICE, since they decrease the readability
    a lot, this is just for your information, you should avoid using them when writing code
"""

"""
    Suppose we want to create a function which prints all numbers that are divisible by 13 and 
    are less than the user input

    Note: we could have done in a more smart way by adding 13 each time, however this is given
    just to demonstrate how continue works
"""
# since we are only printing we do not have to return anything here
def find_all_divisible_continue(number):
    current = 0 # smallest number

    while current < number:
        # a%b returns the remainder as a result of integer division a/b, for example 7 % 2 = 1 and 8 % 4 = 0
        if current % 13 != 0:
            current = current + 1    
            continue

        print(f"{current} is less than {number}")
        current = current + 1

# let's refer to the power of two program from the previous example
# instead of using condition to exit the while loop we could have used break to exit the loop
def find_all_powers_of_two_break(number):
    current_power_of_two = 1 # 2^0 = 1, choose smallest here to start with

    while True:
        if current_power_of_two >= number:
            break 

        print(f"{current_power_of_two} is less than {number}")
        current_power_of_two = current_power_of_two * 2    # multiply by 2 to get the next power


if __name__=="__main__":
    user_number = int(input("Please enter a positive number: "))
    find_all_divisible_continue(user_number)
    print("\n\n\n") # print new line a few times to separate the output of two functions
    find_all_powers_of_two_break(user_number)