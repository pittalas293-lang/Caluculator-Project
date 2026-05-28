while True:
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    operator = input("enter operator (+, -, *, /) :")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("cannot divided by zero")
        else:
            result = num1/num2
    else:
        print("invalid operator")
    if operator in ["+", "-", "*","/"] and not (operator == "/" and num2 == 0):
        print("result", result)

    choice = input ("continue another caluculation (yes/no):")
    if choice == "no":
        print ("please close")
        break


