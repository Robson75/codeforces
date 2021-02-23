class AvoidTrygub:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        string_length = int(input())
        in_string = input()
        out_list = sorted(in_string)
        out_string = ''
        for c in out_list:
            out_string += c
        print(out_string)