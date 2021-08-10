print('\nDay 33: Find the Maximum height when coins are arranged in a triangle\n')
#We have N coins which need to arrange in form of a triangle, i.e. first
# row will have 1 coin, second row will have 2 coins and so on, you need
# to tell maximum height which we can achieve by using these N coins.

def coinHeight(coins):
    coins_req, height = 0,0

    for i in range(1,coins):
        if coins_req < coins:
            coins_req += i
            height += 1
        elif coins_req > coins:
            height = height - 1
            break

    return f'\nMaximum Height of a triangle is {height} using {coins} coins'

total_coins = int(input("Enter the total coins: "))
print(coinHeight(total_coins))

