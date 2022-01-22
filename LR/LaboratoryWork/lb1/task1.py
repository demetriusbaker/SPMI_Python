import sys


# menu
def print_menu(symbol: str):
    print("What do you choose?")

    print('1. Draw a square')
    print('2. Draw a tower upside down')
    print('3. Stop')
    print('option. Change print symbol (default: {})'.format(symbol))


# 1
def draw_square(symbol: str):
    try:
        input_message = 'Give a dimension for your construction: '
        dimension = int(input(input_message))

        print()

        for y in range(dimension):
            for x in range(dimension * 2):
                print(symbol, end='')
            print()
    except ValueError:
        print("Incorrect input number!")


# 2
def draw_tower(symbol: str):
    try:
        input_message = 'Give a dimension for your construction: '
        dimension = int(input(input_message))
        space = ''

        print()

        for square in range(dimension):
            for y in range(dimension):
                for x in range(dimension * 2):
                    if square != 0 and x == 0:
                        print(space, end='')
                    print(symbol, end='')
                print()
            dimension -= 2
            space += '  '
    except ValueError:
        print("Incorrect input number!")


# 3
def stop():
    print("Thanks for playing with us!")
    print()
    print("Druk op een toets om door te gaan.")
    sys.exit()


# option
def change_symbol(sym: str):
    default = sym
    try:
        sym = input('Enter needed symbol: ')[0]
    except IndexError:
        sym = default
    finally:
        return sym


if __name__ == '__main__':
    special_symbol = 'Ы'  # ascii-symbol number 219

    while True:
        print_menu(special_symbol)

        choose = input()

        if choose == '1':
            draw_square(special_symbol)
            print()
        elif choose == '2':
            draw_tower(special_symbol)
            print()
        elif choose == '3':
            stop()
        elif choose == 'option':
            special_symbol = change_symbol(special_symbol)
            print()
        else:
            print("Enter a valid choice: 1, 2 or 3!")
            print()
