class HugeBoxesOfAnimalToys:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        box_1 = "Tidak"
        box_2 = "Tidak"
        box_3 = "Tidak"
        box_4 = "Tidak"
        toy_quantities = list(map(int, input().split()))
        neg_values = toy_quantities[0] + toy_quantities[1]
        big_values = toy_quantities[0] + toy_quantities[3]
        small_values = toy_quantities[1] + toy_quantities[2]
        if neg_values % 2 == 0:
            if big_values > 0:
                box_4 = "Ya"
            if small_values > 0:
                box_3 = "Ya"
        else:
            if big_values > 0:
                box_1 = "Ya"
            if small_values > 0:
                box_2 = "Ya"
        print(box_1 + " " + box_2 + " " + box_3 + " " + box_4)
