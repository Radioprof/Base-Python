for i in range(100):
    i+=1
    if 11 <= i <= 14 or (i % 10) == 0:
        print(f"{i} процентов")
    elif i == 1 or (i % 10) == 1:
        print(f"{i} процент")
    elif 2 <= i < 5 or 2 <= (i % 10) < 5:
        print(f"{i} процента")
    elif 5 <= i <= 9 or 5 <= (i % 10) <= 9:
        print(f"{i} процентов")