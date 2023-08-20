# add, subtract, divide, multiply

class OperandError(ValueError):
    pass

class Calculator():
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x,y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        return x / y


print("Select operation:\n")
print("1. Add\n")
print("2. Subtract\n")
print("3. Multiply\n")
print("4. Divide\n")

calculator = Calculator()

while True:
    try:
        choice = input("Select 1, 2, 3, or 4\n")   
        if choice not in ('1', '2', '3', '4'):
            raise OperandError("Invalid operand")
        
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))
        
        if choice == '1':
            print(num1, "+", num2, "=", calculator.add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", calculator.subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", calculator.multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", calculator.divide(num1, num2))

        nextCalculation = input("Do you want to do another calcuation? (yes/no)")
        if nextCalculation == "no":
            break
    except OperandError as e:
        print(e.args)
    except ValueError as e:
        print(f"Invalid input, select a number {e.args}")
