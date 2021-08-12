"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции """

import copy


def hw2_task1(rub=15, cent=50, product=15):
    """Напишите программу, которая считает общую цену. Вводится M рублей и
    N копеек цена, а также количество S товара Посчитайте общую цену в
    рублях и копейках за L товаров.
    Пример:
    Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
    Output: Общая цена 9 рублей 60 копеек"""
    _all = ((rub * 100) + cent) * product
    print("Всего", _all // 100, "рубля(ей)", _all % 100, "копейка(ек)")


def hw2_task2(str_="To live is the rarest thing in the world. "
                   "Most people exist, that is all"):
    """Найти самое длинное слово в введенном предложении.
    Учтите что в предложении
    есть знаки препинания.
    Подсказки:
    - my_string.split([chars]) возвращает список строк.
    - len(list) - количество элементов в списке"""
    str_1 = str_.replace(",", " ").replace(".", " ").replace("?", " ")
    list_1 = str_1.split(" ")
    best = 0
    for i in range(len(list_1)):
        if len(list_1[i]) > len(list_1[best]):
            best = i
    print(list_1[best])


def hw2_task3(_str="abc cde def"):
    """Вводится строка. Требуется удалить из нее повторяющиеся
    символы и все пробелы.
    Например, если было введено "abc cde def", то должно быть выведено
    "abcdef"."""
    _str = _str.replace(" ", "")  # Убираем пробелы в строке
    _str1 = ""
    for i in _str:  # Цикл убирающий все повторения
        if i not in _str1:
            _str1 += i
    print(_str1)  # Вывод строки без повторений


def hw2_task4(_str="A LOT OF problems are HERE"):
    """Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы."""
    little = 0  # Количество маленьких букв
    big = 0  # Количество больших
    for i in _str:
        if "a" <= i <= "z":  # Проверяем является ли буква маленькой
            little += 1
        elif "A" <= i <= "Z":  # Проверяем является ли буква большой
            big += 1

    print("Количество маленьких букв =", little)
    print("Количество больших букв =", big)


def hw2_task5(num=9):
    """Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится"""
    num1, num2 = (0, 1)  # Задаём 1 и 2 число фибоначи
    i = 1
    while i < num:
        num1, num2 = (num2, num1 + num2)  # Алгоритм фибоначи
        i += 1
        if i == num:  # Проверяем является ли заданное число равным нашему
            print(num1)


def hw2_task6(number=123454321):
    """Определите, является ли число палиндромом (читается слева направо и
    справа налево одинаково). Число положительное целое, произвольной длины.
    Задача требует работать только с числами
    (без конвертации числа в строку или что-нибудь еще)"""
    number1 = 0
    number2 = number
    while number2 > 0:  # цикл для преобразования в обратное число
        digit = number2 % 10  # находим последнюю цифру
        number2 = number2 // 10  # убираем последнюю цифру
        number1 = number1 * 10 + digit
        # добавляем разрядность и добавляем последнее число
    if number == number1:
        print("Данное число является полиндромом")
    else:
        print("Данное число не является полиндромом")


def hw2_task7(s_a=3, s_b=4, s_c=5):
    """Даны: три стороны треугольника. Требуется: проверить,
    действительно ли это стороны треугольника. Если стороны определяют
    треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных."""
    # Проверка, являются ли стороны треугольником
    if s_a > s_b + s_c or s_b > s_a + s_c or s_c > s_a + s_a:
        print("Это точно не треугольник")
    else:
        per = (s_a + s_b + s_c) / 2  # Считаем полупериметр
        # Считаем площадь
        area = (per * (per - s_a) * (per - s_b) * (per - s_c)) ** (float(0.5))
        print("Площадь треугольника равна", area)  # Выводим площадь


def hw2_task8_1(h_l="1 2 -3 4 5"):
    """В этом небольшом задании вам дается строка чисел,
    разделенных пробелами,
    и вы должны вернуть самое высокое и самое низкое число.
    Пример:
    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"
    Примечания:
    Все номера действительны Int32- нет необходимость
    чтобы подтвердить их.
    Во входной строке всегда будет присутствовать хотя бы одно число.
    Выходная строка должна состоять из двух чисел, разделенных
    одним пробелом,
    причем наибольшее число должно быть первым."""
    check = h_l.split()
    print("Максимальное число:", max(check), "Минимальное число:", min(check))


def hw2_task8_2(_str="worlds_run_together"):
    """Complete the method/function so that it converts
    dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized
    only if the original word was capitalized
    (known as Upper Camel Case, also often referred to as Pascal case)."""
    _list = _str.replace("-", " ").replace("_", " ")
    _list = _list.title()  # Все слова ставим с заглавной буквы
    _list = _list.split()  # Делаем список
    _str = "".join(_list)  # Соеденяем всю строку
    print(_str)


def hw2_task8_3(_str="XOXO xoxo xoox"):
    """Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case insensitive.
    The string can contain any char."""
    _x = 0  # Счётчик Х
    _o = 0  # Счётчик О
    for i in _str:
        if "x" == i or "X" == i:  # Является ли символ Х
            _x += 1
        elif "o" == i or "O" == i:  # Является ли символ О
            _o += 1
    if _x == _o:  # Сравнение Х и О
        print("True")


def hw2_task8_4(num1=15, num2=50):
    """Implement a function that adds two numbers together and returns
    their sum in binary.
    The conversion can be done before, or after the addition.
    The binary number returned should be a string."""
    _sum = num1 + num2  # Сумма введённых данных
    _bin = ""
    while _sum > 0:  # Переводим в двоичную систему
        _bin = str(_sum % 2) + _bin
        _sum = _sum // 2

    print(_bin)


def hw2_task8_5(_num=65):
    """Write a function that takes an integer as input,
    and returns the number of bits that are equal to one
    in the binary representation of that number.
    You can guarantee that input is non-negative."""
    _bin = ""
    while _num > 0:  # Переводим в двоичную систему
        _bin = str(_num % 2) + _bin
        _num = _num // 2
    bit = len(str(_bin))  # Считаем количество бит
    print(bit)


def hw3_task1(fizzbuzz=1):
    """Напишите программу, которая печатает цифры от 1 до 100,
     но вместо чисел, кратных 3 пишет Fizz,
     вместо чисел кратный 5 пишет Buzz,
     а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""
    while fizzbuzz <= 100:
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
        elif fizzbuzz % 3 == 0:
            print("Fizz")
        elif fizzbuzz % 5 == 0:
            print("Buzz")
        else:
            print(fizzbuzz)
        fizzbuzz += 1


def hw3_task2():
    """List practice
    1 Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    2 Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc'].
    3 Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
    4 Одной строкой удалите элемент  '2a'
    из прошлого списка и напечатайте его.
    5 Скопируйте список и добавьте в него элемент '2a'
    так чтобы в исходном списке этого элемента не было."""
    # 1
    lst = [lst + lst1 for lst in "ab" for lst1 in "bcd"]
    print(lst)
    # 2
    print(lst[::2])
    # 3
    list_ = [list_ + "a" for list_ in "1234"]
    print(list_)
    # 4
    print(list_.pop(1))  # Удалённый элемент списка
    print("Список без 2а", list_)  # Проверка, что список без 2а
    # 5
    list_1 = copy.deepcopy(list_)  # Создаём независимую копию
    list_1.insert(1, "2a")
    print("Исходный список", list_)  # Проверка, что список без 2а
    print("Список с добавлением 2а", list_1)  # Проверка, что список с 2а


def hw3_task3():
    """Tuple practice
    1 Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    2 Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    3 Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    4 Создайте кортеж из одного элемента, чтобы при итерировании по этому
    элементы последовательно выводились значения 1, 2, 3. Убедитесь что len()
    исходного кортежа возвращает 1."""
    # 1
    lst = list("abc")
    tpl = tuple(lst)
    print(tpl)
    # 2
    lst = list(tpl)
    print(lst)
    # 3
    a, b, c = "a", 2, "python"
    print(a, b, c)
    # 4
    tpl1 = ([1, 2, 3],)
    for i in tpl1[0]:
        print(i)
    print("Кортеж выводит: ", tpl1[0])
    print("Длина кортежа: ", len(tpl1))


def hw3_task4(str_="1 1 1 1 2 2 2 3 3"):
    """Дан список чисел. Посчитайте, сколько в нем пар элементов,
    равных друг другу. Считается, что любые два элемента,
    равные друг другу образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""

    lst = str_.split()  # Переводим строку в список
    par = 0
    for i in lst:
        while lst.count(i) > 1:
            par += lst.count(i) - 1  # Считаем количество пар
            lst.remove(i)
    print(par, "пар(ы) чисел в списке")


def hw3_task5(str_="1 2 3 a b c a 3"):
    """Уникальные элементы в списке
    Дан список. Выведите те его элементы,
    которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке,
    в котором они встречаются в списке."""
    lst = str_.split()  # Переводим строку в список
    if len(lst) == len(set(lst)):
        print("Данный список итак уникален!")
    else:
        lst_new = []
        for i in lst:
            if i not in lst_new:
                lst_new.append(i)
        print(lst_new)


def hw3_task6(lst="1 2 0 0 0 3 0 4 0 0 5 0 6 7"):
    """Дан список целых чисел.
    Требуется переместить все ненулевые элементы в левую часть списка,
     не меняя их порядок, а все нули - в правую часть.
     Порядок ненулевых элементов изменять нельзя, дополнительный список
     использовать нельзя, задачу нужно выполнить за один проход по списку.
     Распечатайте полученный список."""
    lst = lst.split()
    for i in (range(len(lst))):
        if lst[i] == "0":
            lst.remove("0")
            lst.append("0")  # Все нули передвигаем в конец
    print(*lst)


def hw4_task1():
    """Создайте словарь с помощью генератора словарей,
    так чтобы его ключами были числа от 1 до 20,
    а значениями кубы этих чисел."""
    gen_dic = {a: a ** 3 for a in range(1, 21)}
    print(gen_dic)


def hw4_task2(cities_search=None, countries_cities=None):
    """Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится."""
    if cities_search is None:
        cities_search = ["Moscow", "Munich", "Grodno", "Odessa"]
    if countries_cities is None:
        countries_cities = ["Russia Moscow Petersburg Novgorod Kaluga",
                            "Ukraine Kiev Lviv Odessa Kharkiv",
                            "Belarus Minsk Brest Grodno Vitebsk",
                            "Germany Berlin Humburg Dresden Munich"
                            ]
    earth = {}
    for str_country_and_cities in countries_cities:
        list_cities = []
        str_country_and_cities = str_country_and_cities.split()
        for cities_of_the_country in str_country_and_cities[1:]:
            list_cities.append(cities_of_the_country)
        earth[str_country_and_cities[0]] = list_cities
    countries = ""
    for i in cities_search:
        for country, cities_of_the_country in earth.items():
            if i in cities_of_the_country:
                countries += country + "\n"
    print(countries)


def hw4_task3(str_one="1 2 3 4 5", str_two="4 5 6 7 8"):
    """Даны два списка чисел. Посчитайте, сколько различных чисел содержится
    одновременно как в первом списке, так и во втором."""
    lst_one = str_one.split()
    lst_two = str_two.split()
    set_lst = set(lst_one + lst_two)
    print(len(set_lst), "Различных чисел в списке")


def hw4_task4(str_one="1 2 3 4 5", str_two="4 5 6 7 8"):
    """Даны два списка чисел.
    Посчитайте, сколько различных чисел входит только в один из этих списков"""
    lst_one = str_one.split()
    lst_two = str_two.split()
    set1 = set(lst_one)
    set2 = set(lst_two)
    set_1 = set1 - set2
    set_2 = set2 - set1
    print("Различных чисел в первой строке: ", len(set_1))
    print("Различных чисел во второй строке: ", len(set_2))


def hw4_task5(**kwargs):
    """Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники и языки,
    которые знает хотя бы один из школьников."""
    if not kwargs:
        kwargs = {"first_student": ["English", "Russian", "Belarusian"],
                  "second_student": ["English", "Russian", "Belarusian",
                                     "German"],
                  "third_student": ["Italian", "Belarusian"],
                  "fourth_student": ["Belarusian", "Spanish"]
                  }
    list_languages_all = []
    for languages in kwargs.values():
        list_languages_all.append(set(languages))
    all_know = set.intersection(*list_languages_all)
    print("Кол-во языков, которые знают все школьники:", len(all_know))
    for lang_all in all_know:
        print(lang_all)
    anyone_know = set.union(*list_languages_all)
    print(
        "Кол-во языков, которые знает хотя бы один школьник:",
        len(anyone_know)
    )
    for lang_one in anyone_know:
        print(lang_one)


def hw4_task6(str_input="еду, еду в чистом поле: "
                        "колокольчик дин-дин-дин... "
                        "страшно, страшно поневоле "
                        "средь неведомых равнин! "
              ):
    """Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или большим
    числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте."""
    # Убираем все знаки препинания на пробелы
    str_input = str_input.replace(",", " ").replace(".", " ").replace("?", " ")
    str_input = str_input.replace(":", " ").replace("-", " ").replace("!", " ")
    # Убираем все двойные пробелы, для корректности split
    pp = "  "
    while pp in str_input:
        str_input = str_input.replace("  ", " ")
    else:
        set_str = set(str_input.split())
    print(len(set_str))


def hw4_task7(num1=120, num2=144):
    """Даны два натуральных числа. Вычислите их наибольший общий делитель
    при помощи алгоритма Евклида (мы не знаем функции и рекурсию)."""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    print("НОД равен", num1 + num2)


all_func_names = dir()
list_used_funcs = []
for name in all_func_names:
    if name.startswith("__"):
        continue
    elif name == "copy":
        continue
    else:
        list_used_funcs.append(name)


def runner(*args):
    if not args:
        for item in list_used_funcs:
            func = globals()[item]
            func()
    else:
        for item in args:
            func = globals()[item]
            func()


runner("hw2_task2", "hw4_task5")
