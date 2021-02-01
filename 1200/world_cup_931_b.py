class WorldCup:

    pass


if __name__ == "__main__":
    in_data = list(map(int, input().split()))
    nr_of_teams = in_data[0]
    id_1 = in_data[1]
    id_2 = in_data[2]
    if nr_of_teams == 2:
        print("Final!")
    elif id_1 <= nr_of_teams // 2 < id_2 or id_2 <= nr_of_teams // 2 < id_1:
        print("Final!")
    else:
        current_round = 1
        pairs = nr_of_teams // 2
        pair_1 = (id_1 + 1) // 2
        pair_2 = (id_2 + 1) // 2
        while pair_1 != pair_2:
            current_round += 1
            pair_1 = (pair_1 + 1) // 2
            pair_2 = (pair_2 + 1) // 2
        print(current_round)


