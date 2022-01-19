price_list = [32.5, 40, 7, 0.5, 124.08, 55, 2, 320.7, 14.0, 2, 19, 7, 55, 0.9, 14.99]
for _price in price_list:
    _price = str(_price)
    price = _price.split('.')
    if len(price) == 2:
        price[1] = price[1].ljust(2, '0')
    else:
        price.append("00")
    print(f'{price[0]} руб. {price[1]} коп.', end=', ')  # последнюю запятую не догадался как убрать по-простому