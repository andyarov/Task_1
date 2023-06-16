'''НА ВХОД ПОДАЮТСЯ ДВА СПИСКА: АВТОМОБИЛИ И ИМЕНА
НЕОБХОДИМО ПОДОБРАТЬ АВТОМОБИЛЬ ВЛАДЕЛЬЦУ НА ОСНОВАНИИ АЛФАВИТНОГО ПОРЯДКА
В СЛУЧАЕ, ЕСЛИ СПИСКИ НЕ ОДИНАКОВЫ ПО ДЛИНЕ, ВЫДАТЬ СООБЩЕНИЕ О ТОМ,
ЧТО КОМУ-ТО НЕ ДОСТАНЕТСЯ АВТОМОБИЛЬ'''

cars = [c for c in input().split()]
names = [n for n in input().split()]
names.sort()
cars.sort()
match = list(zip(names,cars))
print(match)
if len(names)>len(cars):
    print("sold out")