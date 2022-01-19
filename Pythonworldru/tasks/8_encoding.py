import itertools


def XOR_uncipher(source_str, code_key):
    return XOR_cipher(source_str, code_key)


def XOR_cipher(string, key):
    answer = []

    key = itertools.cycle(key)

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)


if __name__ == "__main__":
    print("XOR encoding - task 8")

    print(XOR_cipher("Beer", "1"))
    print(XOR_uncipher("sTTC", "1"))
