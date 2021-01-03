class WasteSorting:
    pass


if __name__ == "__main__":
    nr_of_tests = int(input())
    fit = 'YES'
    for i in range(nr_of_tests):
        can_space = list(map(int, input().split()))
        waste_amount = list(map(int, input().split()))
        if waste_amount[0] > can_space[0] or waste_amount[1] > can_space[1] or waste_amount[2] > can_space[2]:
            fit = 'NO'
        else:
            can_space[0] -= waste_amount[0]
            can_space[1] -= waste_amount[1]
            can_space[2] -= waste_amount[2]
            if can_space[0] + can_space[2] < waste_amount[3] or can_space[1] + can_space[2] < waste_amount[4]:
                fit = 'NO'
            else:
                can_space[2] -= waste_amount[3] - can_space[0]
                if can_space[2] < waste_amount[4] - can_space[1]:
                    fit = 'NO'

    print(fit)
