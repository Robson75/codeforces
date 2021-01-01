class Team:
    pass


if __name__ == "__main__":
    nr_of_problems = int(input())
    solvable = 0

    for i in range(nr_of_problems):
        in_data = input().split()
        can_solve = 0
        for p in in_data:
            can_solve += int(p)
        if can_solve > 1:
            solvable += 1
    print(solvable)
