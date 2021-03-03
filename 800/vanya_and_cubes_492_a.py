class VanyaAndCubes:

    pass


if __name__ == "__main__":
    cubes = int(input())
    height = 0
    floor_cubes = 1
    while cubes > 0:
        height += 1
        cubes -= floor_cubes
        floor_cubes += (height + 1)
        if cubes < 0:
            height -= 1

    print(height)