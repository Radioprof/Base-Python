def thesaurus(*args):
    notebook = {}
    for name in sorted(args):
        key = name[0]
        if notebook.get(key) is None:
            notebook.update({key: [name]})
        else:
            notebook[key] += [name]
    print(notebook)


thesaurus('Ivan', 'Petr', 'Lesha', 'Ilia', 'Ira', 'Lena', 'Larisa', 'Pavel')
