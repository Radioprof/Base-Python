def odd_gen (n):
    for gen_od in range(1, n+1, 2):
        yield gen_od


for i in odd_gen(int(input('Введите кол-во элементов: '))):
    print(i, end=', ')
