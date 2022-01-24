def num_translate(dict):
    key = input("Введите слово на английском: ")
    print(f'Перевод: {dict.get(key)}')


dictionary = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
num_translate(dictionary)
