from sys import argv

users, hobby, us_hob = argv[1:]
with open(fr'{users}\users.csv', 'r', encoding='utf-8') as file_1:
    with open(fr'{hobby}\hobby.csv', 'r', encoding='utf-8') as file_2:
        with open(fr'{us_hob}\users_hobby.txt', 'w', encoding='utf-8') as file_3:
            name = file_1.readline().replace(',', ' ').replace('\n', '')
            hobby = file_2.readline().replace('\n', '')
            while name:
                if hobby:
                    file_3.writelines(f'{name}: {hobby}\n')
                    name = file_1.readline().replace(',', ' ').replace('\n', '')
                    hobby = file_2.readline().replace('\n', '')
                else:
                    file_3.writelines(f'{name}: None\n')
                    name = file_1.readline().replace(',', ' ').replace('\n', '')
            else:
                if hobby:
                    exit(1)
