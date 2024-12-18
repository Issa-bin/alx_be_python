#Prompt for user input 
num1 = float(input("Enter the first number:"))
operation = input("Choose the operation (+, -, *, /):")
num2 = float(input("Enter the second number:"))

#Perform the Calculation Using Match Case
match operation:
    case '+':
        result = num1 + num2

    case '-':
        result = num1 - num2

    case '*':
        result = num1 * num2

    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2

    case '_':
        print("Not Allowed")


#print result
print("The result is {result}")
