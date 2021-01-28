class Dragons:

    pass


if __name__ == "__main__":
    (own_strength, nr_of_dragons) = map(int, input().split())
    dragon_stats = []
    for dragon in range(nr_of_dragons):
        (dragon_strength, extra_life) = map(int, input().split())
        dragon_stats.append((dragon_strength, extra_life))
    alive = True
    while alive and len(dragon_stats) > 0:
        kill = False
        for dragon in dragon_stats:
            if dragon[0] < own_strength:
                own_strength += dragon[1]
                dragon_stats.remove(dragon)
                kill = True
        if not kill:
            alive = False
    if alive:
        print("YES")
    else:
        print("NO")
