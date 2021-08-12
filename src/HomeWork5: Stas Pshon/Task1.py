"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции """


def hw2_task1(rub=15, cent=50, product=15):
    """
    Напишите программу, которая считает общую цену. Вводится M рублей и
    N копеек цена, а также количество S товара Посчитайте общую цену в
    рублях и копейках за L товаров.
    Пример:
    Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
    Output: Общая цена 9 рублей 60 копеек
    """
    _all = ((rub * 100) + cent) * product
    print("Всего", _all // 100, "рубля(ей)", _all % 100, "копейка(ек)")
