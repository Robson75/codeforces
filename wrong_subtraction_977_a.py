class WrongSubtraction:

    pass


if __name__ == "__main__":
    input_values = list(map(int, input().split()))
    value = input_values[0]
    subtractions = input_values[1]
    for i in range(subtractions):
        if value % 10 == 0:
            value = value // 10
        else:
            value = value - 1
    print(value)
