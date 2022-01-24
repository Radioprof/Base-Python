def num_translate(dict):
    key = input("Введите слово на английском: ")
    if key.istitle():
        print(f'Перевод: {(dict.get(key.lower(),"В словаре нет значения")).title()}')
    else:
        print(f'Перевод: {dict.get(key,"В словаре нет значения")}')


dictionary = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
num_translate(dictionary)