from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as f_2:
    position_1 = (int(argv[1]) - 1) * 12
    if position_1 < f_2.seek(0,2):
        f_2.seek(position_1)
        if argv[2].replace('.', '', 1).replace(',', '', 1).isdigit():
            d = (argv[2].replace(",", ".", 1).rjust(10, '0'))
            f_2.write(f'{d}\n')
        else:
            print(f'Не правильно введена сумма')
    else:
        print('Неправильный номер записи. Повторите ввод.')
