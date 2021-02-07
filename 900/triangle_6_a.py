class Triangle:

    pass


if __name__ == "__main__":
    lengths = list(map(int, input().split()))
    lengths = sorted(lengths)
    triangle = 'IMPOSSIBLE'
    if lengths[1] + lengths[2] > lengths[3] or lengths[0] + lengths[1] > lengths[2]:
        triangle = 'TRIANGLE'
    elif lengths[1] + lengths[2] == lengths[3] or lengths[0] + lengths[1] == lengths[2]:
        triangle = 'SEGMENT'
    print(triangle)
