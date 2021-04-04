class Letters:

    pass


if __name__ == "__main__":
    dorms, letters = list(map(int, input().split()))
    rooms = list(map(int, input().split()))
    room_numbers = list(map(int, input().split()))
    for room_number in room_numbers:
        dorm = 1
        while room_number > rooms[dorm - 1]:
            room_number -= rooms[dorm - 1]
            dorm += 1
        print(str(dorm) + ' ' + str(room_number))
