# Write code below 💖

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]

def max_price(a,b):
  prices = [price_at(day) for day in range(a, b+1)]
  return max(prices)

def min_price(a,b):
  prices = [price_at(day) for day in range(a, b+1)]
  return min(prices)


print(price_at(8))
print(max_price(6,10))
print(min_price(6,10))