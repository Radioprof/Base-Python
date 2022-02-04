from json import dump

with open("users.csv", 'r', encoding='utf-8') as file_1:
     with open("hobby.csv", 'r', encoding='utf-8') as file_2:
        hobby = []
        anketa = {}
        for name in file_1:
            anketa.setdefault(name.replace(',', ' ').replace('\n', ''))
        for _hobby in file_2:
            hobby.append(_hobby.replace('\n', ''))
        if len(anketa) < len(hobby):
            exit(1)
        else:
            with open('result.json', 'w', encoding='utf-8') as file_3:
                for key, h in zip(anketa, hobby):
                    anketa[key] = h
                print(anketa)
                dump(anketa, file_3, ensure_ascii=False, indent=4)
