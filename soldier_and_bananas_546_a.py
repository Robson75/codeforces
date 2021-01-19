class SoldierAndBananas:

    pass


if __name__ == "__main__":
    input_values = list(map(int, input().split()))
    cost_0 = input_values[0]
    cash = input_values[1]
    bananas = input_values[2]
    banana_nr = 0
    total_price = 0
    for banana in range(bananas):
        banana_nr += 1
        price = cost_0 * banana_nr
        total_price += price
    borrow = max(0, total_price - cash)
    print(borrow)
