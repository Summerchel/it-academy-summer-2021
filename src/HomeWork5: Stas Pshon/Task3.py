"""Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"""


def get_ranges(lst):
    total = [lst[0]]
    for item in lst[1::]:
        if int(item) - int(total[-1]) == 1:
            total.append(item)
        else:
            if total[0] == total[-1]:
                print(str(total[0]), end=",")
            else:
                print(str(total[0]) + "-" + str(total[-1]), end=",")
            total.clear()
            total.append(item)
    if total[0] == total[-1]:
        print(str(total[0]))
    else:
        print(str(total[0]) + "-" + str(total[-1]))


get_ranges(input().split())

