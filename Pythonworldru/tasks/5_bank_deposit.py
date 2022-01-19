def bank(a, years, coefficient=0.1):
    try:
        totalA = a
        count = 0

        while count < years:
            totalA += totalA * coefficient
            count += 1

        return totalA
    except TypeError:
        return 0


if __name__ == "__main__":
    print("Bank deposit - task 5")

    # Usual deposit
    print(bank(1000, 1))
    print(bank(1000, 5))
    # Finance Pyramid MMM
    print(bank(100, 10, 200))
