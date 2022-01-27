def num_translate(dict_1):
    key = input("Введите слово на английском: ")
    print(f'Перевод: {dict_1.get(key)}')


dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num_translate(dictionary)
