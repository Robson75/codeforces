
class StrangePartition:

    pass


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        (n, x) = map(int, input().split())
        a_list = list(map(int, input().split()))
        max_beauty = 0
        for a in a_list:
            rest = a % x
            if rest == 0:
                q = a // x
            else:
                q = a // x + 1
            max_beauty += q
        # compress a_list into one nr for minimum beauty
        a_sum = sum(a_list)
        if a_sum % x == 0:
            min_beauty = a_sum // x
        else:
            min_beauty = a_sum // x + 1
        print(str(min_beauty) + ' ' + str(max_beauty))
