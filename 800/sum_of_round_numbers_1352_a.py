class SumOfRoundNumbers:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        output = []
        input_nr = input()
        multiplier = 1
        k = 0
        for nr in input_nr[::-1]:

            if nr != '0':
                k += 1
                out_nr = multiplier * int(nr)
                output.append(out_nr)
            multiplier *= 10
        print(k)
        print(*output)


