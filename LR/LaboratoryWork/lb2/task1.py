if __name__ == '__main__':
    print("Enter file name: ")
    fileName = input()

    try:
        file = open(fileName, encoding='utf-8')
    except FileNotFoundError:
        print("Isn't exist some file: ", fileName)
    else:
        information = file.read()
        print(information)

        file.close()
