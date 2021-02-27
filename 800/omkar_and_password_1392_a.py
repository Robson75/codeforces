class OmkarAndPassword:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        password_length = int(input())
        password = set(map(int, input().split()))
        if len(password) == 1:
            print(password_length)
        else:
            print(1)
