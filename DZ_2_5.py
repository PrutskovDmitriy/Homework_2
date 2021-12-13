prices = [57.8, 46.51, 97, 3.07, 12, 34.99, 599, 22.18, 7.53, 6.03, 124.33, 55.9]


def my_price():
    for price in prices:
        price = int(round(price * 100))
        rub = price // 100
        kop = price % 100
        print(f'{rub:02d} руб {kop:02d} коп', end=', ')


my_price()
print('*' * 50)
prices.sort()
my_price()
print('*' * 50)
prices.sort(reverse=True)
prices = prices[:min(5, len(prices))]
my_price()
print('*' * 50)
