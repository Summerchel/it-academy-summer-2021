"""Оформите указанную задачу из прошлых домашних в виде функции и покройте
тестами. Учтите, что в функцию могут быть переданы некорректные значения,
здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные
ситуации сама.

ДЗ 5 задача 3

Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"""


def get_ranges(lst):
    segment = 0
    lst_temp = [[]]
    final_str = ''

    for num in range(len(lst)):
        if num != len(lst) - 1:
            if lst[num] + 1 == lst[num + 1]:
                (lst_temp[segment].append(lst[num]))
            elif lst[num] + 1 > lst[num + 1]:
                raise ValueError("The list should increase and not decrease")
            else:
                lst_temp.append([])
                lst_temp[segment].append(lst[num])
                segment += 1
        else:
            lst_temp[segment].append(lst[num])

    for el in lst_temp:
        if len(el) > 1:
            final_str += str(el[0]) + '-' + str(el[-1]) + ', '
        else:
            final_str += str(el[0]) + ', '

    final_str = final_str.rstrip(', ')

    return final_str
