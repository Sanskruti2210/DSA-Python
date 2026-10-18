'''Given an array prices, where prices[i] represents the stock price on day i, determine the maximum profit you can achieve by buying and selling the stock at most once.
You must buy before selling.'''

prices = [7, 1, 5, 3, 6, 4]

max_profit = 0
min_price = prices[0]

for i in range(len(prices)):
    
    profit = prices[i] - min_price
    min_price = min(min_price,prices[i])
        
    if profit > max_profit:
        max_profit = profit
            
print(max_profit)