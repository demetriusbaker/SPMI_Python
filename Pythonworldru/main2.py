# Chapter 19 -
import math as мать


def getSum(x, y):
    return x + y


def newFunc(n):
    def myFunc(x):
        return x + n

    return myFunc


def none(): pass


def func(a, b, c=2):
    return a + b + c


def function(*args):
    return args


def nameFunction(**kwargs):
    return kwargs


if __name__ == '__main__':
    summ = getSum(45, 64)
    print(summ)

    cat = getSum("presi", "dent")
    print(cat)

    new = newFunc(1000)
    print(new(2000))

    print(none())

    print(func(1, 2))
    print(func(1, 2, 3))
    print(func(a=1, b=3))

    print(function(1, 2, 3, "abcd", '!'))
    print(function(1))

    print(nameFunction(a=1, b=2, c=3))
    print(nameFunction())
    print(nameFunction(a='petuhon'))

    lyambda = lambda x, y: x + y
    print(lyambda(3, 5))
    print(lyambda('a', 'b'))

    print((lambda a, b, c: a * b * c)(2, 3, 4))

    lyambda = lambda *args: args
    print(lyambda(1, 2, 3, 4))

    try:
        k = 1 / 0
    except ZeroDivisionError:
        k = 0

    print(k)

    try:
        k = 1 / 0
    except ArithmeticError:
        # FloatingPointError, OverflowError and ZeroDivisionError
        k = 0

    print(k)

    f = open('1.txt', 'a')
    ints = []
    try:
        for line in f:
            ints.append(int(line))
    except ValueError:
        print('This is not a number! Exit!')
    except Exception:
        print("What's the hell?!")
    else:
        print("These are ok! No exception and error!")
    finally:
        print("I perform always in the end!")
        f.close()
        print('I closed the file.')
        # try -> exceptions -> else -> finally

    b = bytearray(b'hello world!')
    print(b)
    print(b[0])
    b[0] = 105
    print(b)
    for i in range(len(b)):
        b[i] += i
    print(b)


    # with .. as ..:
    # with open('new_file.txt', 'w', encoding='utf-8') as g:
    #     d = int(input())
    #     print('1 / {} = {}'.format(d, 1 / d), file=g)

    class A:
        def g(self):
            return 'hello world'


    a = A()
    b = A()
    a.arg = 1
    b.arg = 2
    print(a.arg)

    a = A()
    print(a.g())


    class B:
        arg = 'Python'

        def g(self):
            return self.arg


    b = B()
    print(b.g())
    b.arg = 'spam'
    print(b.g())


    class C:
        def _private(self):
            print("This is private method!")


    c = C()
    c._private()


    #     class C:
    #         def __private(self):
    #             print("This is private method!")
    #
    #     c = C()
    #     c.__private()

    class Mydict(dict):
        def get(self, key, default=0):
            return dict.get(self, key, default)


    a = dict(a=1, b=2)
    b = Mydict(a=1, b=2)

    b['c'] = 4
    print(b)
    print(a.get('v'))
    print(b.get('v'))

    print(1 + 1)
    print("1" + '1')


    class D:
        def go(self):
            print('Go, A!')


    class E(D):
        def go(self, name):
            print('Go, {}!'.format(name))


    D().go()
    E().go(name="name")


    class F:
        def __init__(self, name):
            self.name = name


    f = F('Vasya')
    print(f.name)


    class Vector2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'Vector2D({}, {})'.format(self.x, self.y)

        def __str__(self):
            return '({}, {})'.format(self.x, self.y)

        def __add__(self, other):
            return Vector2D(self.x + other.x, self.y + other.y)

        def __iadd__(self, other):
            self.x += other.x
            self.y += other.y
            return self

        def __sub__(self, other):
            return Vector2D(self.x - other.x, self.y - other.y)

        def __isub__(self, other):
            self.x -= other.x
            self.y -= other.y
            return self

        def __abs__(self):
            return мать.hypot(self.x, self.y)

        def __bool__(self):
            return self.x != 0 or self.y != 0

        def __neg__(self):
            return Vector2D(-self.x, -self.y)


    vector = Vector2D(3, 4)
    print(vector)
    print(abs(vector))

    vector2 = Vector2D(5, 6)
    print(vector2)
    print(vector2 + vector)
    print(vector2 - vector)
    print(-vector2)
    print(bool(vector))
    print(bool(vector2))

    noneVector = Vector2D(0, 0)
    print(noneVector)
    print(bool(noneVector))


    def my_shiny_new_decorator(function_to_decorate):
        def the_wrapper_around_the_original_function():
            print("I am a code, that handle before the function calling")
            function_to_decorate()
            print("I'm code, that will work after")

        return the_wrapper_around_the_original_function()


    def stand_alone_function():
        print("I'm a simple alone function, you wouldn't dare to change me, would you?")


    stand_alone_function()
    print()


    # stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
    # stand_alone_function_decorated()
    #
    # stand_alone_function = my_shiny_new_decorator(stand_alone_function)
    # stand_alone_function()

    @my_shiny_new_decorator
    def another_stand_alone_function():
        print("Leave me alone")


    # another_stand_alone_function()

    def bread(func):
        def wrapper():
            print()
            func()
            print("<\___/>")

        return wrapper


    def ingredients(func):
        def wrapper():
            print("#tomato#")
            func()
            print("~salad~")

        return wrapper


    def sandwich(food="-ham-"):
        print(food)


    sandwich()

    sandwich = bread(ingredients(sandwich))
    sandwich()
