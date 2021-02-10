
class BallsOfSteel:

    pass


def manhattan_distance(x1, x2, y1, y2):
    dist = abs(x1 - x2) + abs(y1 - y2)
    return dist


if __name__ == "__main__":
    test_cases = int(input())
    output = []
    for t in range(test_cases):
        (balls, k) = map(int, input().split())
        coordinates = []
        for i in range(balls):
            ball_coord = list(map(int, input().split()))
            coordinates.append(ball_coord)
        for c_a in coordinates:
            possible = True
            for c_b in coordinates:
                if manhattan_distance(c_a[0], c_b[0], c_a[1], c_b[1]) > k:
                    possible = False
            if possible:
                output.append(1)
                break
        if not possible:
            output.append(-1)
    for r in output:
        print(r)