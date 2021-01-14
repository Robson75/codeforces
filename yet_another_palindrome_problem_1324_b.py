class YetAnotherPalindromeProblem:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        found = False
        in_string_length = int(input())
        in_string = list(map(int, input().split()))
        for j in range(in_string_length - 2):
            c = in_string[j]
            if not found and c in in_string[j+2:]:
                found = True
                print("YES")
                break
        if not found:
            print("NO")
