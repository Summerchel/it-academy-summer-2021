""" Задача 268

Можно убедиться в том, что существует 23 натуральных числа меньше 1000,
которые делятся без остатка на хотя бы четыре простые числа меньше 100.

Найдите, сколько существует натуральных чисел в пределах 10^16,
которые делятся без остатка на хотя бы четыре различных простых числа,
не превышающих 100.


ПРИМЕЧАНИЕ:
до 10 ** 7 степени работает адекватно и не долго
"""

a = 10 ** 6
list_of_divisor = []
prime_num_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97]


def euler268(count=1):
    count_of_divisor = 0
    while count < a + 1:
        for item in prime_num_list:
            if count % item == 0:
                list_of_divisor.append(count)
                for i in list_of_divisor:
                    if list_of_divisor.count(i) > 3:
                        list_of_divisor.clear()
                        count_of_divisor += 1
        count += 1
    return count_of_divisor


print("Всего существует ", euler268(), "чисел(ла)")
