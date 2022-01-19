def is_year_leap(year):
    firstCondition = year % 4 == 0 and year % 100 != 0
    secondCondition = year % 400 == 0
    return firstCondition or secondCondition


def date(day, month, year):
    try:
        if month <= 0:
            return False

        day_in_month = [
            31,
            29 if is_year_leap(year) else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
        ]

        return day_in_month[month - 1] >= day
    except TypeError:
        return False
    except IndexError:
        return False


if __name__ == "__main__":
    print("Right data - task 7")

    print("09.05.1945", date(9, 5, 1945))  # True
    print("19.01.2022", date(19, 1, 2022))  # True
    print("32.02.2020", date(32, 2, 2020))  # False
    print("28.13.2019", date(28, 13, 2019))  # False
    print("28.00.2019", date(28, 0, 2019))  # False
