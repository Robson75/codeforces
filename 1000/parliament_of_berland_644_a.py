class ParliamentOfBerland:

    pass


if __name__ == "__main__":
    in_values = list(map(int, input().split()))
    nr_of_parliaments = in_values[0]
    rows = in_values[1]
    chairs = in_values[2]
    if chairs * rows < nr_of_parliaments:
        print('-1')
    else:
        p = 0
        for i in range(rows):
            out_row = []
            for j in range(chairs):
                p += 1
                if p <= nr_of_parliaments:
                    out_row.append(p)
                else:
                    out_row.append(0)
            if chairs % 2 == 0 and i % 2 == 0:
                out_row = out_row[::-1]
            print(*out_row)

