class IqTest:

    pass


def test_arithmetic(in_list):
    arithmetic = True
    current_nr = in_list[0]
    dif = in_list[1] - in_list[0]
    for nr in in_list[1:]:
        if nr - current_nr != dif:
            arithmetic = False
        else:
            current_nr = nr
    if arithmetic:
        next = nr + dif
        return next
    else:
        return 42


def test_geometric(in_list):
    geometric = True
    for nr in in_list:
        if nr == 0:
            return False
    else:
        quotient = in_list[1] / in_list[0]
        current_nr = in_list[0]
        for nr in in_list[1:]:
            if nr / current_nr != quotient:
                geometric = False
            else:
                current_nr = nr
        if geometric:
            next = nr * quotient
            if int(next) == 0 or int(next) / nr != quotient:
                return 42
            else:
                return next
        else:
            return 42


if __name__ == "__main__":
    in_numbers = list(map(int, input().split()))
    answer_ari = test_arithmetic(in_numbers)
    answer_geo = test_geometric(in_numbers)
    if answer_ari != 42:
        print(int(answer_ari))
    else:
        print(int(answer_geo))
