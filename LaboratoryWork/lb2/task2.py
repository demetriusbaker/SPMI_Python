class LetterInformation:
    def __init__(self, symbol: str, count: int):
        self.symbol = symbol
        self.count = count


def get_count_of_symbol(symbol, text):
    count = 0
    for t in text:
        if symbol == t:
            count += 1
    return count


class IncorrectExtensionException(Exception):
    pass


if __name__ == '__main__':
    print("Enter text file name: ")
    fileName = input()

    try:
        if not fileName.__contains__(".txt"):
            raise IncorrectExtensionException()

        file = open(fileName, encoding='utf-8')
    except FileNotFoundError:
        print("Isn't exist some file:", fileName)
    except IncorrectExtensionException:
        print("It was used incorrect extension!")
    else:
        information = file.read()

        if len(information) == 0:
            print("This file is empty!")
            file.close()
            exit(0)

        print(information, '\n')

        information = information.lower()

        lettersSet = {s for s in information if s.isalpha()}
        letterInformationList = list[LetterInformation]()

        for lS in lettersSet:
            sym = str(lS)
            count = get_count_of_symbol(sym, information)
            letterInformation = LetterInformation(sym, count)
            letterInformationList.append(letterInformation)

        print("Sorted by letter (alphabet)")
        print()

        letterInformationList = sorted(letterInformationList, key=lambda o: o.symbol)
        for letter in letterInformationList:
            print("{} -> {}".format(letter.symbol, letter.count))

        print()

        print("Sorted by count (max value)")
        print()

        letterInformationList = sorted(letterInformationList, key=lambda o: o.count, reverse=True)
        for letter in letterInformationList:
            print("{} -> {}".format(letter.symbol, letter.count))

        print()

        file.close()
