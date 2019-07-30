import time

def getCoins(n):
    curr_n = n
    coin_amount = 0

    while curr_n > 0:
        # starts off incrementing
        coin_amount = coin_amount + 1
        if curr_n >= 25:
            # it's a quarter, increment
            curr_n = curr_n - 25
            continue

        if curr_n >= 10:
            # it's a dime, increment
            curr_n = curr_n - 10
            continue

        if curr_n >= 5:
            # it's a nickle, increment
            curr_n = curr_n - 5
            continue

        if curr_n >= 1:
            # it's a penny, increment
            curr_n = curr_n - 1
            continue

    return coin_amount


def main():
    n = 982361
    coincount = getCoins(n)
    print("{} cents can be made with {} coins".format(n, coincount))


if __name__ == '__main__':
    main()