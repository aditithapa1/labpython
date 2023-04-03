def takeInput():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+,-,*,/): ")
    return num1, num2, operator
#taking input

def displayResult(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        return
    
    print(num1, operator, num2, "=", result)

num1, num2, operator = takeInput()
displayResult(num1, num2, operator)
#displaying result
