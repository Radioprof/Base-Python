from sys import argv
with open('bakery.csv', 'a', encoding='utf-8') as f_1:
    if argv[1].replace('.', '', 1).replace(',', '', 1).isdigit():
        d = (argv[1].replace(",", ".", 1).rjust(10, '0'))
        f_1.writelines(f'{d}\n')
    else:
        print(f'Не правильно введена сумма')