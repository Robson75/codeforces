import sys


class StringSimilarity:

    pass


if __name__ == "__main__":
    test_cases = int(sys.stdin.readline())
    for t in range(test_cases):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline()
        middle = s[n-1]
        similar_string = ''
        for c in range(n):
            similar_string += middle
        print(similar_string)
