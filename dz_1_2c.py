sum_3 = 0
for num in range(1, 1001):
    if (num % 2) != 0:
        cube = num ** 3 + 17
        sum_dig = 0
        c = cube
        for n in range (10):
            dig = c % 10
            sum_dig += dig
            c //= 10
        if sum_dig % 7 == 0:
            sum_3 += cube
print(sum_3)