class Student:
    def __init__(self, first_name, last_name, mark: float):
        self.first_name = first_name
        self.last_name = last_name
        self.mark = mark


class EmptyFileException(Exception):
    pass


def for_print(students: list[Student]):
    for s in students:
        print(s.first_name, s.last_name, s.mark)
    print()


def get_sum_of_marks(students: list[Student]):
    summary = 0.0
    for s in students:
        summary += s.mark
    return "Total mark's sum: {0:.3f} ({0})".format(summary)


if __name__ == '__main__':
    print("Enter file name: ")
    fileName = input()

    try:
        file = open(fileName, encoding='utf-8')
    except FileNotFoundError:
        print("Isn't exist some file:", fileName)
    else:
        try:
            information = file.read()
            if len(information) == 0:
                raise EmptyFileException()
        except EmptyFileException:
            print("This file is empty:", fileName)
        else:
            try:
                information_strings = information.split('\n')
                students = list()

                for i in range(len(information_strings)):
                    fields = information_strings[i].split(' ')
                    students.append(Student(fields[0], fields[1], float(fields[2])))
            except IndexError:
                print("The file ({}) was fill incorrect!".format(fileName))
            except ValueError:
                print("The file ({}) was fill incorrect!".format(fileName))
            else:
                print("Before sorting:\n")
                for_print(students)

                students = sorted(students, key=lambda obj: "{} {}".format(obj.first_name, obj.last_name))

                print("After sorting:\n")
                for_print(students)

                print(get_sum_of_marks(students))

                file.close()
