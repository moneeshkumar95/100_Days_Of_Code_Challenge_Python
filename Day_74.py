print('Day 74: Coin change problem using Recursion\n')

def coinChangeRec(target, coins):

    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [j for j in coins if j <= target]:
            num_coins = 1 + coinChangeRec(target-i, coins)

            if num_coins < min_coins:

                min_coins = num_coins

    return min_coins

target = 63
coins = [1,5,10,25]
print('Output:',coinChangeRec(target, coins))
