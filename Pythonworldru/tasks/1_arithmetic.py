def arithmetic(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        try:
            return number1 / number2
        except ZeroDivisionError:
            return "Error: division by zero!!!"
    elif operation == "//":
        try:
            return number1 // number2
        except ZeroDivisionError:
            return "Error: division by zero!!!"
    elif operation == "%":
        return number1 % number2
    else:
        return "Unknown operation!"


if __name__ == "__main__":
    print("Arithmetic - task 1")

    print(arithmetic(2, 3, "+"))
    print(arithmetic(8, 1, "-"))
    print(arithmetic(7, 5, "*"))
    print(arithmetic(20, 0, "/"))
    print(arithmetic(20, 5, "/"))
    print(arithmetic(21, 0, "//"))
    print(arithmetic(24, 7, "//"))
    print(arithmetic(70, 3, "%"))
    print(arithmetic(0, 0, "&"))
