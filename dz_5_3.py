from itertools import zip_longest, islice


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Михаил', 'Степан', 'Артем']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

print(len(tutors))
tuple_tutor = (k for k in zip_longest(tutors, klasses) if len(tutors) > len(klasses))
print(type(tuple_tutor))
print(*islice(tuple_tutor, 10))
print(list(islice(tuple_tutor, 3)))
