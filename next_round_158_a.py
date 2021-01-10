class NextRound:

    pass


if __name__ == "__main__":
    (n, k) = map(int, input().split())
    total = 0
    scores = []
    scores = list(map(int, input().split()))
    k_score = scores[k - 1]
    for score in scores:
        if score > 0 and score >= k_score:
            total += 1
    print(total)
