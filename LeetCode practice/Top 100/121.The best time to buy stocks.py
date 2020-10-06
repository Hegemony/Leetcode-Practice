"""
暴力超时
"""
def maxProfit(prices):
    cur_prices, max_prices = 0, 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            cur_prices = prices[j] - prices[i]
            if cur_prices < 0:
                max_prices = max(max_prices, 0)
            else:
                if cur_prices > max_prices:
                    max_prices = cur_prices
    return max_prices


# print(maxProfit([7, 1, 5, 3, 6, 4]))

def maxProfit1(prices):
    n = len(prices)
    if n <= 1:
        return 0
    max_profit = 0
    min_price = prices[0]
    for i in prices:
        min_price = min(i, min_price)
        max_profit = max(i-min_price, max_profit)
    return max_profit

print(maxProfit1([7, 1, 5, 3, 6, 4]))
print(maxProfit1([7, 6, 4, 3, 1]))
print(maxProfit1([]))

