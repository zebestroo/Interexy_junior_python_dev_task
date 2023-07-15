def shift(ls, coin):
    """
        This function implements shift for elements in list(ls).
        The shift value is coin.
        Example:
            For list = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0] and coin = 2
            Shifted list = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
        Each element shifts for coin value
    """

    test_list = ls[:-coin]

    for i, elem in enumerate(test_list):
        ls[i + coin] = test_list[i]

    return ls
    

def foo():
    """
        This function implements main algorithm.
        We check each coin for its necessity of presence in list of necessary coins.
        Coin not necessary if there is a pattern of another coins with sum(coins) = x.
        If this pattern exists, we skip coin and mark it as not necessary coin.
    """

    for index in range(len(coins_list)):
        check_list = coins_list[0:index] + coins_list[index+1:]
        template = [1] + [0] * x
        necessary = True

        for elem in check_list:

            template = shift(template, elem)
            if template[-1] == 1:
                necessary = False
                break

        if necessary:
            necessary_coins.append(coins_list[index])


if __name__ == '__main__':
    import time


    n, x = (int(param) for param in input().split(' '))
    coins_list = [int(coin) for coin in input().split(' ')]

    # start = time.time()

    necessary_coins = []
    foo()

    print(len(necessary_coins))
    print(' '.join([str(coin) for coin in necessary_coins]))

    # print("Processing time is ", time.time() - start)
