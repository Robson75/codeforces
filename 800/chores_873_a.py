class Chores:

    pass


if __name__ == "__main__":
    n, k, x = list(map(int, input().split()))
    chore_times = list(map(int, input().split()))
    for i in range(1, k + 1):
        chore_times[-i] = x
    print(sum(chore_times))
