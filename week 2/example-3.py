"""
    Each execution cycle of a loop is called iteration
    “continue” statement makes the loop immediately proceed to the next iteration
    “break” statement makes the loop exit immediately

    continue and break statements are considered a BAD PRACTICE, since they decrease the readability
    a lot, this is just for your information, you should avoid using them when writing code
"""

"""
    Suppose we want to create a function which prints all powers of two less than a particular
    number, but also skips all powers of two that are divisible by 8 (1, 2, 4)
"""
# since we are only printing we do not have to return anything here
def find_all_powers_of_two_continue(number):
    current_power_of_two = 1 # 2^0 = 1, choose smallest here to start with

    while current_power_of_two < number:
        # a%b returns the remainder as a result of integer division a/b, for example 7 % 2 = 1 and 8 % 4 = 0
        if current_power_of_two % 8 == 0:
            current_power_of_two = current_power_of_two * 2    # multiply by 2 to get the next power
            continue

        print(f"{current_power_of_two} is less than {number}")
        current_power_of_two = current_power_of_two * 2    # multiply by 2 to get the next power

# instead of using condition to exit the while loop we could have used break to exit the loop
# Note this version finds all powers of two including these that are divisible by 8
def find_all_powers_of_two_break(number):
    current_power_of_two = 1 # 2^0 = 1, choose smallest here to start with

    while True:
        if current_power_of_two >= number:
            break 

        print(f"{current_power_of_two} is less than {number}")
        current_power_of_two = current_power_of_two * 2    # multiply by 2 to get the next power


if __name__=="__main__":
    user_number = int(input("Please enter a positive number: "))
    find_all_powers_of_two_continue(user_number)
    print("\n\n\n") # print new line a few times to separate the output of two functions
    find_all_powers_of_two_break(user_number)