firstNum = input("Enter the first number: ")
operation = input("Select an operation (+, -, *, /, %) : ")
secondNum = input("Enter the second number: ")

if operation == '+':
    print(int(firstNum) + int(secondNum))
elif operation == '-':
    print(int(firstNum) - int(secondNum))
elif operation == '*':
    print(int(firstNum) * int(secondNum))
elif operation == '/':
    print(int(firstNum) / int(secondNum))
elif operation == '%':
    print(int(firstNum) % int(secondNum))
else:
    print("Invalid Selection!")