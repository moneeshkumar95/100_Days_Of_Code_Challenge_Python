print('Day 86\n')


def solution(unsorter_prices, max_price):

    prices_to_counts = [0] * (max_price + 1)

    for price in unsorter_prices:
        prices_to_counts[price] += 1

    sorted_prices = []

    for price, count in enumerate(prices_to_counts):

        for time in range(count):
            sorted_prices.append(price)

    return sorted_prices

print('Output:')
print(solution([8,2,6,3,9,7,5,4], 9))