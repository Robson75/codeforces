from operator import itemgetter
import bisect


class Berpizza:

    pass


if __name__ == "__main__":
    nr_of_queries = int(input())
    guest_nr = 0
    serving_nr = 0
    serve_order = []
    guest_queue = []
    prio_order = []
    for q in range(nr_of_queries):
        query = list(map(int, input().split()))
        if query[0] == 1:
            guest_nr += 1
            priority = query[1]
            if len(prio_order) == 0:
                prio_order.append((guest_nr, priority))
            else:
                for i in range(len(prio_order)):
                    if prio_order[i][1] < priority:
                        if i == 0:
                            prio_order = [(guest_nr, priority)] + prio_order
                        else:
                            prio_order = prio_order[0:i-1] + [(guest_nr, priority)] + prio_order[i + 1:]
                    if i == len(prio_order) - 1:
                        prio_order.append((guest_nr, priority))
            guest_queue.append((guest_nr, priority))
        elif query[0] == 2:
            served_guest = guest_queue.pop(0)
            prio_order.remove(served_guest)
            serve_order.append(served_guest[0])
        elif query[0] == 3:
            prio_guest = prio_order.pop(0)
            serve_order.append(prio_guest[0])
            guest_queue.remove(prio_guest)
    print(*serve_order)
