class TripForMeal:

    pass


if __name__ == "__main__":
    visits = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    distances = [a , b , c]
    total_distance = 0
    if visits > 1:
        if c < a and c < b:
            if a < b:
                total_distance += a
                total_distance += (visits - 2) * c
            else:
                total_distance += b
                total_distance += (visits - 2) * c
        elif a < b:
            total_distance += (visits - 1) * a
        else:
            total_distance += (visits - 1) * b
    print(total_distance)