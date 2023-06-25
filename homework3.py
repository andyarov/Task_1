from random import sample
from math import factorial
from itertools import permutations

'''1. Напишите программу, принимающую на вход слова через запятую
и выводящую слова в алфавитном порядке. Используйте List comprehension.'''
def srt():
    words = [w for w in input().split(",")]
    words.sort()
    return words
print(srt())

'''2. Напишите программу принимающую на вход список [1,2,3]
и выводящую все возможные комбинации его членов.: 
Ответ: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)'''
dgts = [1, 2, 3]
rslt = []
def permutations_without_itertools(dgts,rslt):
    while len(rslt) < factorial(len(dgts)):
        lst = sample(dgts, len(dgts))
        tpl = tuple(lst)
        if tpl not in rslt:
            rslt.append((tpl))

    print(sorted(rslt))
permutations_without_itertools(dgts,rslt)
'''3. Изучите функцию permutations из itertools.
Напишите программу выводящую все возможные варианты для списка [1,2,3]
'''
digits = [1,2,3]
# digits = [int(d) for d in input().split(",")]
def ittls_prmt(digits):
    permut = [digits for digits in permutations(digits)]
    return permut

print(ittls_prmt(digits))

'''4. Используя random.sample сгенерируйте список случайных элементов.
Используйте List comprehension.'''
lst = [i for i in input().split()]
qt = int(input("enter the number of list items:",))
def random_elem(lst, qt):
    try:
        elem = [e for e in sample(lst, qt)]
        return elem
    except ValueError:
        print('Sample larger than population')
print(random_elem(lst,qt))

'''5. Напишите функцию которая принимает на вход неограниченное количество аргументов,
а на выходе возвращает их сумму. Используйте *args.'''
def sum_args(*args):
    return sum(args)
print(sum_args(3,4,5,6,7,8))