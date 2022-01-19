def is_prime(number):
    try:
        if isinstance(number, int) and number not in range(2, 1001):
            return False

        size = int(number / 2 + 1)
        for x in range(2, size):
            if number % x == 0:
                return False

        return True
    except TypeError:
        return False


if __name__ == "__main__":
    print("Prime - task 6")

    for i in range(0, 1001):
        if is_prime(i):
            print(i, end=" ")
