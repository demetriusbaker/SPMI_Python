import math as m


def square(side_length):
    try:
        if side_length < 0.0:
            return ()

        perimeter = side_length * 4
        square = pow(side_length, 2)
        diagonal_length = m.sqrt(2) * side_length
        return perimeter, square, diagonal_length
    except TypeError:
        return ()


if __name__ == "__main__":
    print("Square - task 3")

    print(square("32r2"))
    print(square(-8))
    print(square(0))
    print(square(1))
    print(square(m.sqrt(2)))
    print(square(m.pi))
    print(square(5))
    print(square(7))
    print(square(23.9))
