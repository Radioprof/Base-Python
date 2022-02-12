import re

e_mailstr = re.compile(r'([a-z0-9_-]+)(@)([a-z0-9_\.-]+\.[a-z]{,4})', re.IGNORECASE)
def email_parse(addr):
    b = {}
    if e_mailstr.match(addr):
        a = re.split(r'@', addr)
        b[a[0]] = a[1]
        return b
    else:
        raise ValueError(f'wrong email: {addr}')



addr_ls = ['test_adr2022@maTil.ru', 'retr@gmcom', 'testaddr_y48-@mail.ru']
for a in addr_ls:
    try:
        print(email_parse(a))
    except ValueError as er:
        print(er)