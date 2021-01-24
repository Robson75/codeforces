class BovineDilemma:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        nr_of_trees = int(input())
        tree_coordinates = list(map(int, input().split()))
        base_distances = set()
        for coordinate_1 in tree_coordinates:
            for coordinate_2 in tree_coordinates:
                if coordinate_2 - coordinate_1 > 0:
                    base_distances.add(coordinate_2 - coordinate_1)
        print(len(base_distances))
