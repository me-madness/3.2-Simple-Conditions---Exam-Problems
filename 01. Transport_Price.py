n = int(input())
day = input()

price = 0
day_tarife = 0

if day == 'day':
    day_tarife = 0.79
else:
    day_tarife = 0.90
    
if n < 20:
    price = n * day_tarife + 0.70
elif n < 100:
    day_tarife = 0.09
    price = n * day_tarife
else:
    day_tarife = 0.06 
    price = n * day_tarife
    
print(price)   