class SearchForPrettyIntegers:

    pass


if __name__ == "__main__":
    (n, m) = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list = sorted(a_list)
    b_list = list(map(int, input().split()))
    b_list = sorted(b_list)
    found = False
    for nr in a_list:
        if nr in b_list and not found:
            smallest = nr
            found = True
            break
    if not found:
        if a_list[0] < b_list[0]:
            smallest = a_list[0] * 10 + b_list[0]
        else:
            smallest = b_list[0] * 10 + a_list[0]
    print(smallest)


