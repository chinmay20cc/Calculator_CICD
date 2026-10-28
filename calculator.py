def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a/b
def main():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    print("Python calculator")
    print("Enter first number:",a)
    print("Enter the second number:",b)
    print("Addition:",add(a,b))
    print("Subtraction:",subtract(a,b))
    print("Multiplication:",multiply(a,b))
    print("Division:",divide(a,b))

if __name__ == "__main__":
    main()