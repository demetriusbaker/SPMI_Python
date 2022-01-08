import math
import random


def print_hi(_):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {_}')  # Press Ctrl+F8 to toggle the breakpoint.


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

    i = 0
    while i < 10:
        print(i)
        i += 1

    for i in "hello world":
        print(i)

    print()

    for i in "hello world":
        print(i, end='')

    print()

    for i in "hello world":
        print(i * 2, end='')

    print()

    for i in "abcdefgh":
        if i == 'e':
            break
        elif i == 'b':
            continue
        else:
            print(i, end='')

    print()

    for i in "пиво":
        if i == 'a':
            break
        else:
            print(i, end='')
    else:
        print()
        print("В пиве нет буквы а (а в водке - есть)")

    print()

    print(20 // 3)  # 6
    print(20 % 3)  # 2
    print(3 ** 4)  # 81
    print(pow(3, 4))  # 81
    print(pow(3, 4, 27))  # 0
    print(3 ** 150)
    # 369988485035126972924700782451696644186473100389722973815184405301748249

    n = -37
    print(bin(n))
    print(n.bit_length())

    print((1024).to_bytes(2, byteorder='big'))
    # b'\x04\x00'
    print((1024).to_bytes(10, byteorder='big'))
    # b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
    print((-1024).to_bytes(10, byteorder='big', signed=True))
    # b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
    x = 1000
    print(x.to_bytes((x.bit_length() // 8) + 1, byteorder='little'))
    # b'\xe8\x03'

    print(int.from_bytes(b'\xe8\x03', byteorder='big'))
    print(int.from_bytes([255, 0, 0], byteorder='big'))

    number = 19
    print(bin(number))
    print(hex(number))
    print(oct(number))

    print(int('1010', 2))
    print(int('1010'))

    c = 150
    d = 12.9
    print(c + d)
    print(c - d)

    p = abs(c - d)
    print(p)
    print(round(p))

    print(math.pi)
    print(math.sqrt(2))

    print(random.random())

    x = complex(1, 2)
    print(x)

    y = complex(3, 4)
    print(y)

    z = x + y
    print(x)

    print(z)

    z = x * y
    print(z)

    z = x / y
    print(z)

    print(x.conjugate())  # Сопряжённое число

    print(x.imag)  # Мнимая часть

    print(x.real)  # Действительная часть

    # print(x > y)  # Комплексные числа нельзя сравнить

    print(x == y)  # Но можно проверить на равенство

    abs(3 + 4j)  # Модуль комплексного числа

    pow(3 + 4j, 2)  # Возведение в степень

    string = """
    fds
    dfs
    dsf
    dsf
    """
    print(string)

    s1 = "spam"
    s2 = 'egg'
    print(s1 + s2)

    print('dima' * 8)

    print(len('Dietmar Granda'))

    print("0123456789"[8])
    print("0123456789"[-8])

    print("баварское пиво - топ!"[10:14])
    print("beer$#FD"[:4])
    print("whole word"[:])
    print("$$dollar"[2:])
    print("0101010101010101"[2:5:2])
    print("0101010101010101"[::2])
    print("esrever"[::-1])

    print('Hello, {}!'.format("Arseniy!"))
    print("{0} {1} {2}".format('a', 'b', "c"))
    print('value: {value}'.format(value="Жигуль шестерка!"))

    coordinates = {'latitude': 37.24, 'longitude': -115.81}
    print('Coordinates: ({latitude}, {longitude})'.format(**coordinates))

    c = [1, 2, 3]
    print(c)

    c = [i * 8 for i in '♂dungeon master♂']
    print(c)

    pyList = [5, 34, 6345, 653, 65, 43, 64, 7783, 54, 7]
    print(pyList)
    pyList.sort()
    print(pyList)
    pyList.append(8)
    print(pyList)
    print(pyList.index(653))
    pyList.remove(8)
    print(pyList)
    pyList.reverse()
    print(pyList)

    a = [1, 2, 3, 4]
    a[1:4] = [6, 6, 6]

    print(a)

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(b[4:7])

    c = [1, 0, 0, 0, 7]
    del c[:-3]
    print(c)

    print(())
    print(tuple())
    print('s')
    print('s', )
    print(('s',))
    print(tuple('hello world!'))

    a = 2
    b = 3
    print("a={a} and b={b}".format(a=a, b=b))

    a, b = b, a
    print("a={a} and b={b}".format(a=a, b=b))

    print({})
    print({'dict': 1, 'dictionary': 2})
    print(dict(short='dict', long='dictionary'))
    print(dict([(1, 1), (2, 4)]))
    print(dict.fromkeys(['a', 'b']))
    print(dict.fromkeys(['a', 'b'], 100))
    print({a: a ** 2 for a in range(7)})

    print(set())
    print(set('hello'))
    print({'a', 'b', 'c', 'c', 'd', 'a'})
    print({i ** 2 for i in range(10)})

    words = ['hello', 'daddy', 'hello', 'num']
    print(set(words))

    a = set('qwerty')
    b = frozenset('qwerty')
    print(a == b)
    # frozenset as usual set, but immutable!


