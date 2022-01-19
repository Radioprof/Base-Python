dam_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for new_rec in dam_list:
    name = new_rec.title()[new_rec.rindex(" "):]
    print(f"Привет, {name}!")