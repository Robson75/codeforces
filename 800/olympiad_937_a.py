class Olympiad:

    pass


if __name__ == "__main__":
    participants = int(input())
    scores = set(map(int, input().split()))
    scores.add(0)
    print(len(scores) - 1)
