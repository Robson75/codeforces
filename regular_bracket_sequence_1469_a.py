class RegularBracketSequence:
    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        in_sequence = input()
        if len(in_sequence) % 2 != 0 or in_sequence[0] == ')' or in_sequence[-1] == '(':
            print('NO')
        else:
            print('YES')
