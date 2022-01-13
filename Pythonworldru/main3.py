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


if __name__ == '__main__':
    print_full_name("Vasya", "Pupkin")

    lucy = Lucy()
    lucy.sayYourAge(-3)

    # 130/154
