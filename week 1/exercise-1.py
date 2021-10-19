""" 
    Defining functions. Please note we do not have to separate area or perimeter logic
    into separate functions, the program would still be correct. However, it is a best practice
    to separate self-contained functionality (commonly referred to as separation of concerns).
    
    
    Quick note about functions:
        
        def func(param1, param2):
            return param1 + param2
        
        defines a function called "func" which takes in 2 parameters and returns their sum.
        
        When the program execution hits the return statement it exits the function and
        sends the return value to the place in the program where the function was called.
        
        For example, 
        
        a = func(10, 20) -> after this statement a will be equal to 30, since func returns the sum.
        Essentially func(10,20) is substituted with the actual value (30), so it is equivalent to saying
        a = 30
        
        print(func(10,20)) -> same idea here, it is equivalent to print(30)
        
        We may pass variables into the function as parameters and the variable names DO NOT 
        have to match the parameter names, for example:
        
        num1 = 10
        num2 = 20
        print(func(num1, num2)) is transferred into print(func(10, 20)) and finally into print(30)
        
        We may have multiple return statements in the function, where each return statement 
        corresponds to a particular case in the conditional execution, see examples in week 2.
        
        
"""
def find_area(w, h):
    return w * h

def find_perimeter(w, h):
    return 2 * (w + h)

def main():
    width = int(input("Please enter width of the rectangle: "))
    height = int(input("Please enter height of the rectangle: "))

    area = find_area(width, height)
    perimeter = find_perimeter(width, height)

    print(f"The area of the rectangle with sides {width} and {height} is {area}")
    print(f"The perimeter of the rectangle with sides {width} and {height} is {perimeter}")

if __name__ == "__main__":
    main()


