"""
    Suppose you are working for an amusement park company and you need to write a program
    that checks that the client’s age is greater than 14 to make sure that it will be safe
    for them to be on a particular attraction.
    Write a program that outputs “YES” if the client’s age is greater than 14 and 
    “NO” if the client’s age is less than or equal to 14. 
    If the age entered is invalid, i.e the number is less than zero notify the user about by printing “ERROR”

"""

"""
    We use all UPPER CASE letters if we want to let other programmers know that the variable is not going
    to change (constant).
"""
REQUIRED_AGE = 14 

"""I provide three versions of the function."""

def check_age_version_1(age):
    if age > REQUIRED_AGE:   # takes care of age > 14
        return "YES"
    elif age >= 0:           # is only executed if age > 14 failed, hence takes care of age <=14 and age >=0
        return "NO"          # which can be written as 0<=age<=14
    else:                   
        return "ERROR"       # is executed when all else fails, hence age < 0

def check_age_version_2(age):

    if age < 0:
        return "ERROR"       # early return makes sure that if the program reaches later statements
                             # age will be greater or equal to 0

    if age > REQUIRED_AGE:  # takes care of age > 14
        return "YES"
    else:
        return "NO"         # since age >=0 which just return no: it is less than required age and is valid

def check_age_version_3(age):
    answer = "NOT DEFINED"  # we can use a variable to store the result and then return it at the end

    # the answer will be correct since only one of the if, elif and else will be executed
    if age > REQUIRED_AGE:
        answer = "YES"
    elif age >= 0:
        answer = "NO"
    else:
        answer = "ERROR"

    return answer 


# sometimes we may not want to have a top-level main() function we can execute some statements
# in the entry point directly

if __name__ == "__main__":
    age = int(input("Please enter client's age: "))

    # print the value returned by different versions
    print(f"Version 1: {check_age_version_1(age)}")     #note we can use f-strings with function calls directly
    print(f"Version 2: {check_age_version_2(age)}")
    print(f"Version 2: {check_age_version_3(age)}")