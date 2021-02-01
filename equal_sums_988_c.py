class EqualSums:

    pass


def find_positions(sums_list):
    possible = False
    i_poss = 0
    j_poss = 0
    x = 0
    y = 0
    out_list = []
    for i, p_sums_i in enumerate(possible_sums_list):
        for j, p_sums_j in enumerate(possible_sums_list):
            if j != i:
                for index_i, sum_i in enumerate(p_sums_i):
                    for index_j, sum_j in enumerate(p_sums_j):
                        if sum_i == sum_j:
                            possible = True
                            x = index_i + 1
                            y = index_j + 1
                            i_poss = i + 1
                            j_poss = j + 1
                            out_list = [i_poss, j_poss, x, y]
                            return out_list
    return out_list


if __name__ == "__main__":
    nr_of_sequences = int(input())
    possible_sums_list = []
    for s in range(nr_of_sequences):
        length = int(input())
        sequence = list(map(int, input().split()))
        sequence_sum = sum(sequence)
        possible_sums = set()
        for nr in sequence:
            possible_sums.add(sequence_sum - nr)
        possible_sums_list.append(possible_sums)

    possible_data = find_positions(possible_sums_list)

    if possible_data:
        print("YES")
        print(str(possible_data[0]) + " " + str(possible_data[2]))
        print(str(possible_data[1]) + " " + str(possible_data[3]))
    else:
        print("NO")
