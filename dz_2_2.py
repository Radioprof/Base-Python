test_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = ""
for i in range(len(test_list)):
    test_str = test_list[i]
    if test_str.isdigit() is True:
        test_str = '"' + test_str.zfill(2) + '"'
    elif test_str.startswith(('+', '-')) is True:
        _test_str = test_str[0]
        test_str = '"' + _test_str + test_str[1:].zfill(2) + '"'
    result = result + test_str + " "
    test_list[i] = test_str
result = " ".join(test_list)
print(f'Преобразованный список: {test_list}')
print(f'Результат: "{result.rstrip()}"')  # убираем пробел в конце строки
