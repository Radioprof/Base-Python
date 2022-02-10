import os
from collections import defaultdict

res = defaultdict(list)
root_path = "some_data"

for _root, _dir, _file in os.walk(root_path):
    for item in _file:
        b = os.path.join(_root, item)
        size_f = (os.stat(b)).st_size
        for n in range(2, 8):
            r_size = 10**n
            if size_f <= r_size:
                gf = res[r_size]
                if len(res[r_size]) == 0:
                    res[r_size].append(1)
                else:
                    res[r_size][0] += 1
                if item.split('.')[1] not in res[r_size]:
                    res[r_size].append(item.split('.')[1])
                break
# print(f'В каталлоге файлов объемом:')
for key, f in res.items():
    res[key] = tuple(f)
    # print(f'-до {key} Б - {f[0]}, тип - {tuple(f[1:])}')

print(res)
