import functools
import time


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Look, what i got:", arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name's", first_name, last_name)


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)

    return wrapper


class Lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I'm {} years old, and how much would you give?".format(self.age + lie))


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Sent me anything?")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_arguments():
    print('Python is cook, no arguments here.')


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not?"):
    print("Do they like {}, {} and {} - platypuses? {}".format(a, b, c, platypus))


class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=3):
        print("I'm {} years old, and how much would you give?".format(self.age + lie))


def decorator_marker():
    print("I create decorators! I will call only once: when you ask me to create decorator")

    def my_decorator(func):
        print("I - decorator! I will call only once: on function's decorating moment")

        def wrapped():
            print("I am a wrapper around the function to be decorated.")
            print("I will call every time you call a decorated function.")
            print("I return the result of decorated function.")
            return func()

        print("I am returning a wrapped function.")
        return wrapped

    print("I am returning a decorator.")
    return my_decorator


def decorated_function():
    print("I am a decorated function.")


def foo():
    print("foo")


def bar(func):
    def wrapper():
        print("bar")
        return func()

    return wrapper


@bar
def foo1():
    print("foo")


def bar1(func):
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()

    return wrapper


@bar
def foo2():
    print("foo")


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res

    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} was called: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@benchmark
@logging
@counter
def reverse_string(string):
    return ''.join(reversed(string))


if __name__ == '__main__':
    print_full_name("Vasya", "Pupkin")

    lucy = Lucy()
    lucy.sayYourAge(-3)

    function_with_no_arguments()
    function_with_arguments(1, 2, 3)
    function_with_named_arguments("Bill", 'Linus', "Steve", platypus="Exactly!")

    mary = Mary()
    mary.sayYourAge()

    new_decorator = decorator_marker()
    decorated_function = new_decorator(decorated_function)
    decorated_function()

    print(foo.__name__)
    print(foo1.__name__)
    print(foo2.__name__)

    print(reverse_string("And the rose fell on the paw of Azor"))
    print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, acoloratura,"
                         "maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag,"
                         "a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash,"
                         "a jar, sore hats, a peon, a canal: Panama!"))

    print()

