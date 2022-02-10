import os

dir_path = {"my_project": [{"settings": []}, {"mainapp": []}, {"adminapp": []}, {"authapp": []}]}
for _dir, _subdirs in dir_path.items():
    for subdir in _subdirs:
        for path in subdir.keys():
            _a = os.path.join(_dir, path)
            if not os.path.exists(_a):
                os.makedirs(_a)
            else:
                print(f'Объект {_a} уже существует')
