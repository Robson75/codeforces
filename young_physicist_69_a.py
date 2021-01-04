class YoungPhysicist:
    pass


if __name__ == "__main__":

    nr_of_forces = int(input())
    force_components_tot = [0, 0, 0]
    for force in range(nr_of_forces):
        force_components = list(map(int, input().split()))
        force_components_tot = [sum(x) for x in zip(force_components_tot, force_components)]
    if force_components_tot == [0, 0, 0]:
        print('YES')
    else:
        print('NO')
