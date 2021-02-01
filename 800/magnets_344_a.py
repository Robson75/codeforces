import sys


class Magnets:

    pass


if __name__ == "__main__":
    nr_of_magnets = int(sys.stdin.readline())
    groups = 1
    last_magnet = sys.stdin.readline()
    for n in range(1, nr_of_magnets):
        m = sys.stdin.readline()
        if m != last_magnet:
            groups += 1
        last_magnet = m
    print(groups)


