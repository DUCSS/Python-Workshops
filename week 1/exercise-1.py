""" 
    Defining functions. Please note we do not have to separate area or perimeter logic
    into separate functions, the program would still be correct. However, it is a best practice
    to separate self-contained functionality (commonly referred to as separation of concerns).
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


