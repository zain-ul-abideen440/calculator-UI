from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please try again.")
                continue
            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        choice = input("Do you want to quit? (Y/N): ").strip().lower()
        if choice == 'y':
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
