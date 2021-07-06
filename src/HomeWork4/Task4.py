"""Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков"""

str_one = input("Введите первый список через пробел: ")
str_two = input("Введите второй список через пробел: ")
lst_one = str_one.split()
lst_two = str_two.split()
set1 = set(lst_one)
set2 = set(lst_two)
set_1 = set1 - set2
set_2 = set2 - set1
print("Различных чисел в первой строке: ", len(set_1))
print("Различных чисел во второй строке: ", len(set_2))
