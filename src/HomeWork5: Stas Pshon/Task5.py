"""Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)"""


def nearest_of_two(num, power_of_two):
    while num - (2 ** power_of_two) >= 0:
        power_of_two += 1
    module = abs(num - (2 ** power_of_two))
    # Считаем через модуль, что бы минус не попортил результат
    t_in_p = 2 ** (power_of_two - 1)
    # Два в степени, для удобства записи
    if module > num - t_in_p:
        print("Ближайшее число: ", t_in_p)
    elif module == num - t_in_p:
        print("Близжайшие числа: ")
    else:
        print("Ближайшее число: ", t_in_p * 2)


nearest_of_two(int(input("Введите число для проверки: ")), 0)
