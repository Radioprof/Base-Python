test_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = ""
for test_str in test_list:
    if test_str.isdigit() is True:
        test_str = '"' + test_str.zfill(2) + '"'
    elif test_str.startswith(('+', '-')) is True:
        _test_str = test_str[0]
        test_str = '"' + _test_str + test_str[1:].zfill(2) + '"'
    result = result + test_str + " "
print(f'Результат: "{result[:-1]}"')  # убираем пробел в конце строки