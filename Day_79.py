print('Day 79\n')

def profit(stock_prices):

    if len(stock_prices) < 2:
        raise Exception('Need atleast two stock prices')

    min_stock_price = stock_prices[0]

    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        comparision_profit = price - min_stock_price

        max_profit = max(max_profit, comparision_profit)

        min_stock_price = min(min_stock_price, price)

    return max_profit


print('Output:',profit([34,21,16,20]))
print('\nOutput:',profit([28,15,10,26,18]))
