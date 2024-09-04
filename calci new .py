def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Math Error!"

while True:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Select operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    option = input("Enter the option to select operation: ")
    if option == '1':
        result = add(a, b)
        operation = "addition"
    elif option == '2':
        result = subtract(a, b)
        operation = "subtraction"
    elif option == '3':
        result = multiply(a, b)
        operation = "multiplication"
    elif option == '4':
        result = divide(a, b)
        operation = "division"
    elif option == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid input! Please select a valid option.")
        continue
    print(f"The result of {operation} is: {result}")
