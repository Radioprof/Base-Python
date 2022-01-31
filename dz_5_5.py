src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 25, 16, 25, 11, 9, 88]
result = [el for el in src if src.count(el) == 1]
print(*result)


src_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 25, 16, 25, 11, 9, 88]
dic_2 = {}
for i in src_2:
    dic_2.setdefault(i, [])
    dic_2[i] += [i]
# result_2 = (n,k for n,k in dic_2() if len(k) == 1)
print(*(n for n, k in dic_2.items() if len(k) == 1))
