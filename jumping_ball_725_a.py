class JumpingBall:

    pass


if __name__ == "__main__":
    nr_of_bumpers = int(input())
    bumper_types = list(input())
    fall_bumpers = 0
    bumper_index = 0
    while bumper_index < nr_of_bumpers and bumper_types[bumper_index] == '<':
        fall_bumpers += 1
        bumper_index += 1
    bumper_index = nr_of_bumpers - 1
    while bumper_index >= 0 and bumper_types[bumper_index] == '>':
        fall_bumpers += 1
        bumper_index -= 1
    print(fall_bumpers)
