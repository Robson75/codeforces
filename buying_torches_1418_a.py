import math


class BuyingTorches:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        start_sticks = 1
        in_variables = list(map(int, input().split()))
        sticks_gained_trade_1 = in_variables[0] - 1
        sticks_used_trade_2 = in_variables[1]
        torches_required = in_variables[2]
        total_sticks_used_trade_2 = torches_required * sticks_used_trade_2
        trades_first_option = math.ceil(total_sticks_used_trade_2 / sticks_gained_trade_1)
        trades_second_option = torches_required
        sticks_over = trades_first_option * sticks_gained_trade_1 + start_sticks - total_sticks_used_trade_2
        if sticks_over == 0:
            trades_first_option += 1
            sticks_over = sticks_gained_trade_1
        sticks_still_needed = torches_required - sticks_over
        trades_first_option += math.ceil(sticks_still_needed / sticks_gained_trade_1)
        trades_total = trades_first_option + trades_second_option

        print(trades_total)
