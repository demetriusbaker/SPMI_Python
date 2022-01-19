def season(year_number):
    if isinstance(year_number, int):
        if year_number in range(1, 3):
            return "winter"
        elif year_number in range(3, 6):
            return "spring"
        elif year_number in range(6, 9):
            return "summer"
        elif year_number in range(9, 12):
            return "fall"
        else:
            return "winter"
    else:
        return "Unknown type!"


if __name__ == "__main__":
    print("Season - task 4")

    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    for i in range(len(months)):
        print("{}({}): {}".format(months[i], i + 1, season(i + 1)))
