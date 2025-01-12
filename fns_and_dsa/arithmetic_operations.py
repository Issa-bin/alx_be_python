from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")

    num1 = float( input("Enter the first number: "))
    num2 = float( input("Enter the second number: "))
    operation = input ("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    #Perform operations
    result = perform_operation(num1,num2,operation)

    if result == "Division by zero":
      print("Error: Division by zero")
    else:
      print(f"Result: {result}")

def perform_operation(num1, num2, operation):
    """
    Performs the specified arithmetic operation on two numbers.

    Args:
    num1: The first number.
    num2: The second number.
    operation: The operation to perform. Must be one of 'add', 'subtract', 'multiply', or 'divide'.

    Returns: 
     The result of the operation. If the operation is 'divided' and num2 is zero, returns the string "Division by zero".
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
      if num2 == 0:
        return "Division by zero"
      else: 
        return num1/num2
    else:
      raise ValueError(f"Invalid operation: {operation}")

if __name__== "__main__":
    main()
