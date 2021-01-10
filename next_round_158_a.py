class NextRound:

    pass


if __name__ == "__main__":
    (n, k) = map(int, input().split())
    to_next_round = 0
    scores = list(map(int, input().split()))
    k_score = scores[k - 1]
    for score in scores:
        if score > 0 and score >= k_score:
            to_next_round += 1
    print(to_next_round)
