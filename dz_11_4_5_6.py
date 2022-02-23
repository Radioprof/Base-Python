class ErrEnter(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:
    ls_store = {}
    ls_dep = {}
    capacity = 200

    # dep_name - название ДЕПАРТАМЕНТА, dep_org-название орг.техники, dep_num -кол-во
    @staticmethod
    def st_out(dep_name, org_name, org_num):
        if org_name in Store.ls_store:
            if Store.ls_store[org_name] >= org_num:
                Store.ls_store[org_name] -= org_num
                Store.capacity += org_num
                if dep_name in Store.ls_dep:
                    if org_name in Store.ls_dep[dep_name]:
                        Store.ls_dep[dep_name][org_name] += org_num
                    else:
                        Store.ls_dep[dep_name][org_name] = org_num
                else:
                    Store.ls_dep[dep_name] = {org_name: org_num}
            else:
                print('Этого оборудования не достаточно на складе')
        else:
            print('Этого оборудования нет на складе')
        return Store.ls_dep

    @staticmethod
    def st_in(org_name, org_num):
        try:
            if org_name.istitle():
                if org_num > Store.capacity:
                    print(f'{org_num} не умещается на склад')
                else:
                    if org_name in Store.ls_store:
                        Store.ls_store[org_name] += org_num
                    else:
                        Store.ls_store[org_name] = org_num
                    Store.capacity -= org_num
                return Store.ls_store
            else:
                raise ErrEnter('Название техники должно начинаться с заглавной буквы.')
        except ErrEnter as err:
            print(err)


class OrgTech:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.num = number


class Printers(OrgTech):
    def __init__(self, name, price, number, speed_pr, type_pr):
        OrgTech.__init__(self, name, price, number)
        self.sp_pr = speed_pr
        self.type_pr = type_pr


class Scaners(OrgTech):
    def __init__(self, name, price, number, f_paper, color=True):
        OrgTech.__init__(self, name, price, number)
        self.f_paper = f_paper
        self.color = color


class Copiers(OrgTech):
    def __init__(self, name, price, number, speed_cop, paper_num):
        OrgTech.__init__(self, name, price, number)
        self.speed_cop = speed_cop
        self.paper_num = paper_num


# ОТЛАДКА:
org_1 = Printers('Epson', 200, 5, 20, 'laser')
org_2 = Scaners('HP', 150, 3, 'A4')
org_3 = Copiers('Kiosera', 320, 4, 30, 500)
org_4 = Printers('Canon', 230, 7, 23, 'laser')
org_5 = Printers('canon', 230, 7, 23, 'laser')
a = Store()
c = Store()
print(a.capacity)
a.st_in(org_5.name, org_5.num)
a.st_in(org_1.name, org_1.num)
a.st_in(org_2.name, org_2.num)
a.st_in(org_3.name, org_3.num)
a.st_in(org_4.name, org_4.num)
c.st_out('бухгалтерия', 'Canon', 2)
c.st_out('бухгалтерия', 'Canon', 3)
c.st_out('бухгалтерия', 'Epson', 2)
c.st_out('бухгалтерия', 'Xerox', 2)
c.st_out('бухгалтерия', 'Canon', 8)
print(Store.ls_store)
print(Store.ls_dep)
print(a.capacity)
a.st_in('Canon', 300)
