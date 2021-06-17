"""Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке"""

_str = input("Введите строку: ")
_str1 = _str.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ").replace(":", " ").replace(";", " ")
_list = _str1.split(" ")
best = 0
for i in range(len(_list)):
  if len(_list[i]) > len(_list[best]):
    best = i
print(_list[best])
