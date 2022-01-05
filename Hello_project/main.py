
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print("F")

    number = int(input("Enter number: "))
    if number > 100:
        print("More, than 100, current number: ", number)
    elif 50 <= number <= 100:
        print("Between 50 to 100, current number: ", number)
    else:
        print("Less, than 50, current number: ", number)

    name = input("Enter name: ")
    res = 1000 if "Dietrich" == name else 100
    print(res)

    variable = 666
    print(variable)
    variable = "Santa-sa-santa-y-satan"
    print(variable)

