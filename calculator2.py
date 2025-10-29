def get_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please choose +, -, *, or /.")

def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def main():
    print("Welcome to the Campus Calculator!")
    
    while True:
        num1 = get_valid_number("Enter the first number: ")
        num2 = get_valid_number("Enter the second number: ")
        operation = get_valid_operation()
        
        result = perform_calculation(num1, num2, operation)
        print(f"The result is: {result}")
        
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Campus Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
