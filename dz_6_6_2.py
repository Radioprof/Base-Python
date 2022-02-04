from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    st_line, sp_line = [1, None]
    if len(argv[1:]) == 1:
        st_line = argv[1]
    elif len(argv[1:]) == 2:
        st_line, sp_line = argv[1:]
    f.seek((int(st_line) - 1) * 12)
    line = f.readline()
    if sp_line is None:
        while line:
            print(line, end='')
            line = f.readline()
    else:
        while f.tell() <= (int(sp_line) * 12):
            print(line, end='')
            line = f.readline()
