price_list = [32.5, 40, 7, 0.5, 124.08, 55, 2, 320.7, 14.0, 2, 19, 7, 55, 0.9, 14.99]
print(f'Исходный список цен: {price_list}')
print(f'Адрес списка: {id(price_list)}')
price_list.sort()
new_price_list = price_list[::-1]
print(f'Отсортированный по возрвстанию список: {price_list}')
print(f'Адрес списка: {id(price_list)}')
print(f'Отсортированный по убыванию новый список: {new_price_list}')
print(f'Адрес списка: {id(new_price_list)}')
print(f'Пять самых дорогих товаров: {price_list[-5:]}')