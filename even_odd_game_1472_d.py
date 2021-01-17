class EvnOddGame:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        list_length = int(input())
        number_list = list(map(int, input().split()))
        number_list = sorted(number_list)
        number_list = [nr for nr in number_list[::-1]]
        i = 0
        score_bob = 0
        score_alice = 0
        for nr in number_list:
            i += 1
            if i % 2 == 0:
                if nr % 2 != 0:
                    score_bob += nr
            else:
                if nr % 2 == 0:
                    score_alice += nr
        if score_bob > score_alice:
            print("Bob")
        elif score_bob < score_alice:
            print("Alice")
        else:
            print("Tie")

