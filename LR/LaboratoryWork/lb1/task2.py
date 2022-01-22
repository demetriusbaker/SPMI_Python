import random
import math

X_CODE = 'X'
O_CODE = 'O'

SCRIPTS = (
    'Continue!',
    'You won!',
    'Computer won!',
    'Draw!'
)

fields = ['1', '2', '3',
          '4', '5', '6',
          '7', '8', '9']


def guess_computer():
    max_value = len(fields) - 1
    random_number_position = random.randint(0, max_value)

    while (fields[random_number_position] == X_CODE or
           fields[random_number_position] == O_CODE):
        if random_number_position != max_value:
            random_number_position += 1
        else:
            random_number_position = 0
    fields[random_number_position] = X_CODE


def guess_user():
    number_position = -1
    minimum_index = 0
    maximum_index = len(fields) - 1

    while number_position not in range(minimum_index, maximum_index):
        key_board_input = input("Enter position's number (from 1 to 9): ")
        try:
            number_position = int(key_board_input) - 1
        except ValueError:
            print("Incorrect input!")
            number_position = -1
        else:
            if number_position not in range(minimum_index, maximum_index + 1):
                print('This number is not in this range!')
                continue

            if (fields[number_position] != X_CODE and
                    fields[number_position] != O_CODE):
                break
            else:
                print("This field is already occupied!")
                number_position = -1

    fields[number_position] = O_CODE


def check_field(sign):
    won = False

    for i in range(0, 9, 3):
        if fields[i] == sign and fields[i + 1] == sign and fields[i + 2] == sign:
            won = True
            break

    if not won:
        for i in range(0, 3):
            if fields[i] == sign and fields[i + 3] == sign and fields[i + 6] == sign:
                won = True
                break

    if not won:
        if fields[0] == sign and fields[4] == sign and fields[8] == sign:
            won = True
        elif fields[2] == sign and fields[4] == sign and fields[6] == sign:
            won = True

    draw = True

    for f in fields:
        if f.isdigit():
            draw = False
            break

    if won:
        if sign == O_CODE:
            return SCRIPTS[1]
        else:
            return SCRIPTS[2]
    elif draw:
        return SCRIPTS[3]
    else:
        return SCRIPTS[0]


def print_field():
    play_field = """
    +-----------+-----------+-----------+
    |           |           |           |
    |           |           |           |
    |     {}     |     {}     |     {}     |
    |           |           |           |
    |           |           |           |
    +-----------+-----------+-----------+
    |           |           |           |
    |           |           |           |
    |     {}     |     {}     |     {}     |
    |           |           |           |
    |           |           |           |
    +-----------+-----------+-----------+
    |           |           |           |
    |           |           |           |
    |     {}     |     {}     |     {}     |
    |           |           |           |
    |           |           |           |
    +-----------+-----------+-----------+
        """
    print(play_field.format(
        fields[0],
        fields[1],
        fields[2],
        fields[3],
        fields[4],
        fields[5],
        fields[6],
        fields[7],
        fields[8]))


if __name__ == '__main__':
    while True:
        guess_computer()
        print_field()
        check_result = check_field(X_CODE)
        if check_result != SCRIPTS[0]:
            print(check_result)
            break

        guess_user()
        print_field()
        check_result = check_field(O_CODE)
        if check_result != SCRIPTS[0]:
            print(check_result)
            break
