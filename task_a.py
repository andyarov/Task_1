'''На входе список чисел, требуется вывести
максимальное
минимальное
все числа, которые делятся на 3 и не делятся на 5'''

lst = [5,4,3,2,1,13,45,67,87,89,90,657,15,851,32]
min = lst[0]
max = lst[0]
digits = []
for i in lst:
  if min >= i:
    min = i
  elif max <= i:
    max = i
  if i % 3 == 0 and i % 5 != 0:
    digits.append(i)
print("max = ", max)
print("min = ", min)
print(digits)