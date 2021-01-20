class ReplacingElements:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        in_data = list(map(int, input().split()))
        n = in_data[0]
        d = in_data[1]
        in_list = list(map(int, input().split()))
        in_list = sorted(in_list)
        if in_list[-1] <= d or in_list[0] + in_list[1] <= d:
            print("YES")
        else:
            print("NO")
