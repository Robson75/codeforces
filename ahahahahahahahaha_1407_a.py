class Ahahahahahahahaha:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        list_length = int(input())
        number_list = list(map(int, input().split()))
        out_list = []
        i = 0
        while i < len(number_list):
            if i < len(number_list) - 2:
                if number_list[i] == number_list[i + 1]:
                    out_list.append(number_list[i])
                    out_list.append(number_list[i + 1])
                    i += 2
                elif number_list[i + 1] == number_list[i + 2]:
                    out_list.append(number_list[i + 1])
                    out_list.append(number_list[i + 2])
                    i += 3
                else:
                    out_list.append(number_list[i])
                    out_list.append(number_list[i + 2])
                    i += 3
            elif i < len(number_list) - 1:
                if number_list[i] == number_list[i + 1]:
                    out_list.append(number_list[i])
                    out_list.append(number_list[i + 1])
                elif number_list[i] == 0:
                    out_list.append(number_list[i])
                else:
                    out_list.append(number_list[i + 1])

                i += 2
            else:
                if len(out_list) % 2 != 0:
                    out_list.append(number_list[i])
                i += 1
        print(len(out_list))
        out_string = ''
        for nr in out_list:
            out_string += str(nr) + " "
        print(out_string[:-1])
