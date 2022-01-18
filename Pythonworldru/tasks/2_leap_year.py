def is_year_leap(year):
    def check_year(year):
        firstCondition = year % 4 == 0 and year % 100 != 0
        secondCondition = year % 400 == 0
        return firstCondition or secondCondition

    if isinstance(year, int):
        return check_year(year)
    elif isinstance(year, str):
        try:
            return check_year(int(year))
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":
    print("Leap year - task 2")

    print("1992 - ", is_year_leap(1992))
    print("2000 - ", is_year_leap(2000))
    print("1900 - ", is_year_leap(1900))
    print('"1992" - ', is_year_leap("1992"))
    print('"2000" - ', is_year_leap("2000"))
    print('"1900" - ', is_year_leap("1900"))
    print('"it\'s text, not number!" - ', is_year_leap("it's text, not number!"))
    print("{} - ", is_year_leap({}))
