def calculate():  # basic calculator
    case1 = float(input("Enter your number: "))
    op = input("What's your operator (+, -, /, *): ")
    case2 = float(input("Enter another number: "))

    if op == "+":
        return case1 + case2
    elif op == "-":
        return case1 - case2
    elif op == "/":
        return case1 / case2
    elif op == "*":
        return case1 * case2
    else:
        return "Please input a valid operator"
