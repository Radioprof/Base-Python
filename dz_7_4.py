import os
from collections import defaultdict

res = defaultdict(int)
root_path = "some_data"
for _root, _dir, _file in os.walk(root_path):
    for item in _file:
        b = os.path.join(_root, item)
        size_f = (os.stat(b)).st_size
        for n in range(2,8):
            r_size = 10**n
            if size_f <= r_size:
                res[r_size] += 1
                break
print(res)
