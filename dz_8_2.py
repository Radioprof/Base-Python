import re

pars_temp = re.compile(r'(\d{1,3}(\.\d{1,3}){3})(.+[[]\b)(\b\d{2}/[A-Za-z]+/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})(.{2}[\'"\b])([A-Z]+)[\s]([\b/]\S+)(\b\s\S+\s\b)(\d+)[\s](\d+)')


def str_pars(log_str, _n):
    if pars_temp.match(log_str):
        parsed_raw = re.match(pars_temp, log_str)
        print(_n, parsed_raw[1], parsed_raw[4], parsed_raw[6], parsed_raw[7], parsed_raw[9], parsed_raw[10])
    else:
        raise ValueError(f'wrong string: {n}')


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    n = 1
    for raw in f:
        try:
            str_pars(raw, n)
        except ValueError as er:
            print(er)
        n += 1
