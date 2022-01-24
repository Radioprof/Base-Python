def thesaurus_adv (*args):
    notebook = {}
    _y = []
    _z = {}
    for x in args:
        _y.append(x[(x.index(" ") + 1):])
    _y.sort()
    for i in _y:
        y = i[0]
        notebook[y] = {}
    for w in sorted(args):
        key_1 = w[w.index(" ") + 1]
        key_2 = w[0]
        if key_2 in notebook[key_1]:
            notebook[key_1][key_2] += [w]
        else:
            notebook[key_1][key_2] = [w]
    return (notebook)


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
# print(f'thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"')