"""
    Suppose you want to print all powers of 2 which are less than a particular number
    that the user inputs.
    A power of 2 is a number of the form 2^k where k is positive integer or zero, for example:
    2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 =16 …
"""

# since we are only printing we do not have to return anything here
def find_all_powers_of_two(number):
    current_power_of_two = 1 # 2^0 = 1, choose smallest here to start with

    while current_power_of_two < number:
        print(f"{current_power_of_two} is less than {number}")
        current_power_of_two = current_power_of_two * 2    # multiply by 2 to get the next power


if __name__=="__main__":
    user_number = int(input("Please enter a positive number: "))
    find_all_powers_of_two(user_number)