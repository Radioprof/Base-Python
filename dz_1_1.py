duration = int(input("Введите промежуток времени в сек. : "))
if duration < 0:
    print ("Число не может быть отрицательным!")
else:
    day = duration // 86400
    hour = duration % 86400 // 3600
    mnt = duration % 86400 % 3600 // 60
    sec = duration % 60
    print(f"Это составляет {day} дн {hour} час {mnt} мин {sec} сек.")