class ILovePUsernameP:
    pass


if __name__ == "__main__":
    nr_of_contests = int(input())
    points = list(map(int, input().split()))
    amazing = 0
    min_points = points[0]
    max_points = points[0]
    for p in points[1::]:
        if p < min_points:
            amazing += 1
            min_points = p
        elif p > max_points:
            amazing += 1
            max_points = p
    print(amazing)
