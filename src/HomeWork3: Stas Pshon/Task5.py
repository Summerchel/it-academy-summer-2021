"""Уникальные элементы в списке
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке."""

str_ = input('Введите список через пробел: ')
lst = str_.split()  # Переводим строку в список
lst_new = []
for i in lst:
    if i not in lst_new:
        lst_new.append(i)
print(lst_new)
