class Dungeon:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        beautiful = "YES"
        health_points = list(map(int, input().split()))
        if sum(health_points) % 9 != 0:
            beautiful = "NO"
        else:
            enhanced_shots = sum(health_points) // 9
            for health in health_points:
                if enhanced_shots > health:
                    beautiful = "NO"
        print(beautiful)
