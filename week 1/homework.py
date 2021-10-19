"""
    The division operator in python: /
    Integer division: result is also an integer, for example 2/3 = 0 (since 2 = 0 * 3 + 2), or 
    7/2 = 3 (since 7 = 3 * 2 + 1)

    Floating point division: result can be a floating point number (decimal):
    7.0/2 = 3.5 

    Note python will assume that the division is integer if there are no floating point numbers
    involved in it. If a = 5 and b = 2, then a/b is an integer division, to make it floating
    point division: (1.0*a)/b. 

    If at least one of the numbers is floating point then the result is floating point:

    a = 9.0, b = 2

    a/b = 4.5

"""

def mean(a, b, c, d):
    return (a + b + c + d)/4.0 

if __name__ == "__main__":

    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    c = int(input("Input three number: "))
    d = int(input("Input four number: "))

    print(f"Mean of ({a}, {b}, {c}, {d}) is {mean(a, b, c, d)}")