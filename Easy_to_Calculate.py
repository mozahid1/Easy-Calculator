
# This function adds two numbers
def add(x,y):
    return x + y

# This function subtracts two numbers
def subtract(x,y):
    return x - y

# This function multiplies two numbers
def multiply(x,y):
    return x * y

# This function divides two numbers
def divide(x,y):
    return x / y


print("Select Your Operation:-")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # Take input from the user
    choice = input("Enter choice(between 1 to 4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Try Again")
