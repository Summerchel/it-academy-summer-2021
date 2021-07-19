"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции """

import copy

"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара Посчитайте общую цену в рублях и копейках за
L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек"""


def product_sum():
    rub = int(input("Сколько рублей стоит товар:  "))
    cent = int(input("Сколько копеек стоит товар: "))
    product = int(input("Сколько товара: "))
    _all = ((rub * 100) + cent) * product
    print("Всего", _all // 100, "рубля(ей)", _all % 100, "копейка(ек)")


"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении
есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке"""


def largest_word():
    _str = input("Введите строку: ")
    _str1 = _str.replace(",", " ").replace(".", " ").replace("?", " ")
    _list = _str1.split(" ")
    best = 0
    for i in range(len(_list)):
        if len(_list[i]) > len(_list[best]):
            best = i
    print(_list[best])


"""Вводится строка. Требуется удалить из нее повторяющиеся
символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено
"abcdef"."""


def excess_symbols():
    _str = input("Введите строку для преобразования: ")  # Вводим строку
    _str = _str.replace(" ", "")  # Убираем пробелы в строке
    _str1 = ""
    for i in _str:  # Цикл убирающий все повторения
        if i not in _str1:
            _str1 += i
    print(_str1)  # Вывод строки без повторений


"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы."""


def little_big():
    _str = input("Введите текст: ")
    little = 0  # Количество маленьких букв
    big = 0  # Количество больших
    for i in _str:
        if "a" <= i <= "z":  # Проверяем является ли буква маленькой
            little += 1
        elif "A" <= i <= "Z":  # Проверяем является ли буква большой
            big += 1

    print("Количество маленьких букв =", little)
    print("Количество больших букв =", big)


"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""


def fibonacci():
    n = int(input("Введите какое число фибоначи нужно вывести: "))
    num1, num2 = (0, 1)  # Задаём 1 и 2 число фибоначи
    i = 1
    while i < n:
        num1, num2 = (num2, num1 + num2)  # Алгоритм фибоначи
        i += 1
        if i == n:  # Проверяем является ли заданное число равным нашему
            print(num1)


"""Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково). Число положительное целое, произвольной длины. Задача
требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)"""


def palindrome():
    number = int(input("Введите положительное целое число: "))
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


"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это
стороны треугольника. Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных."""


def square():
    s_a = float(input("Введите сторону А: "))  # Вводим А
    s_b = float(input("Введите сторону B: "))  # Вводим В
    s_c = float(input("Введите сторону C: "))  # Вводим С
    # Проверка, являются ли стороны треугольником
    if s_a > s_b + s_c or s_b > s_a + s_c or s_c > s_a + s_a:
        print("Это точно не треугольник")
    else:
        per = (s_a + s_b + s_c) / 2  # Считаем полупериметр
        # Считаем площадь
        area = (per * (per - s_a) * (per - s_b) * (per - s_c)) ** (float(0.5))
        print("Площадь треугольника равна", area)  # Выводим площадь


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


def high_low():
    h_l = list(map(int, input("Введите список чисел через пробел: ").split()))
    print("Максимальное число:", max(h_l), "Минимальное число:", min(h_l))


"""Complete the method/function so that it converts
dash/underscore delimited words into camel casing.
The first word within the output should be capitalized
only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case)."""


def camel():
    _str = input("Введите строку через - или _:")
    _list = _str.replace("-", " ").replace("_", " ")
    _list = _list.title()  # Все слова ставим с заглавной буквы
    _list = _list.split()  # Делаем список
    _str = "".join(_list)  # Соеденяем всю строку
    print(_str)


"""Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char."""


def xo_check():
    _str = input("Введите строку: ")
    _x = 0  # Счётчик Х
    _o = 0  # Счётчик О
    for i in _str:
        if "x" == i or "X" == i:  # Является ли символ Х
            _x += 1
        elif "o" == i or "O" == i:  # Является ли символ О
            _o += 1
    if _x == _o:  # Сравнение Х и О
        print("True")


"""Implement a function that adds two numbers together and returns
their sum in binary.
The conversion can be done before, or after the addition.
The binary number returned should be a string."""


def num_to_bin():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    _sum = num1 + num2  # Сумма введённых данных
    _bin = ""
    while _sum > 0:  # Переводим в двоичную систему
        _bin = str(_sum % 2) + _bin
        _sum = _sum // 2

    print(_bin)


"""Write a function that takes an integer as input,
and returns the number of bits that are equal to one
in the binary representation of that number.
You can guarantee that input is non-negative."""


def num_bit():
    _num = int(input("Введите число: "))
    _bin = ""
    while _num > 0:  # Переводим в двоичную систему
        _bin = str(_num % 2) + _bin
        _num = _num // 2
    bit = len(str(_bin))  # Считаем количество бит
    print(bit)


"""Напишите программу, которая печатает цифры от 1 до 100,
 но вместо чисел, кратных 3 пишет Fizz,
 вместо чисел кратный 5 пишет Buzz,
 а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""


def fizz_and_buzz():
    fizzbuzz = 1
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


def list_practice():
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


"""Tuple practice
1 Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2 Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3 Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4 Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3. Убедитесь что len()
исходного кортежа возвращает 1."""


def tuple_practice():
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


"""Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""


def pairs():
    str_ = input('Введите числа через пробел: ')
    lst = str_.split()  # Переводим строку в список
    par = 0
    for i in lst:
        while lst.count(i) > 1:
            par += lst.count(i) - 1  # Считаем количество пар
            lst.remove(i)
    print(par, "пар(ы) чисел в списке")


"""Уникальные элементы в списке
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке."""


def uni_elements():
    str_ = input('Введите список через пробел: ')
    lst = str_.split()  # Переводим строку в список
    if len(lst) == len(set(lst)):
        print("Данный список итак уникален!")
    else:
        lst_new = []
        for i in lst:
            if i not in lst_new:
                lst_new.append(i)
        print(lst_new)


"""Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка,
 не меняя их порядок, а все нули - в правую часть.
 Порядок ненулевых элементов изменять нельзя, дополнительный список
 использовать нельзя, задачу нужно выполнить за один проход по списку.
 Распечатайте полученный список."""


def not_null_elements():
    lst = input("Введите числа через пробел: ").split()
    for i in (range(len(lst))):
        if lst[i] == "0":
            lst.remove("0")
            lst.append("0")  # Все нули передвигаем в конец
    print(*lst)


"""Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел."""


def dict_gen():
    gen_dic = {a: a ** 3 for a in range(1, 21)}
    print(gen_dic)


"""Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится."""


def countries():
    earth = {}
    n_num = int(input("Сколько стран будем вводить? "))
    for item in range(n_num):
        country_city = input("Введите сначало страну, потом город(а): ")
        country_city = country_city.split()
        cities = country_city[1:]  # Список только городов
        country = country_city[0]
        earth[country] = cities  #
    m_num = int(input("Сколько городов будем проверять? "))
    list_countries = ""
    for index in range(m_num):  # Цикл от 0 до M
        city_find = input("Введите город: ")
        for country_find, in_country in earth.items():
            if city_find in in_country:
                list_countries += country_find
    for printed_city in list_countries:
        print(printed_city)


"""Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором."""


def set_different():
    str_one = input("Введите первый список через пробел: ")
    str_two = input("Введите второй список через пробел: ")
    lst_one = str_one.split()
    lst_two = str_two.split()
    set_lst = set(lst_one + lst_two)
    print(len(set_lst), "Различных чисел в списке")


"""Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков"""


def set_diff_in_one():
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


"""Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников."""


def schoolboy():
    all_lang = set()  # Языки которые знают все школьники
    any_lang = set()  # Все языки, которые знают школьники
    cur_lang = set()  # Языки текущего ученика, для проверки
    n = int(input("Введите количество учеников: "))
    for i in range(1, n + 1):
        mi = int(input(f"Сколько языков знает {i}-й ученик? "))
        for y in range(1, mi + 1):
            lang = input(f"Введите {y}-й язык {i}-го ученика ")
            any_lang.add(lang)
            cur_lang.add(lang)
        all_lang = all_lang.intersection(cur_lang) if all_lang else cur_lang
        cur_lang = set()
    lst_all, lst_any = list(all_lang), list(any_lang)
    print("Всего языков которые знают все:", len(lst_any))
    for q in range(len(lst_all)):
        print(lst_all[q])
    print("Всего языков:", len(lst_any))
    for w in range(len(lst_any)):
        print(lst_any[w])


"""Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте."""


def diff_words_str():
    str_input = input("Введите строку: ")
    # Убираем все знаки препинания на пробелы
    str_input = str_input.replace(",", " ").replace(".", " ").replace("?", " ")
    str_input = str_input.replace(":", " ").replace(";", " ").replace("!", " ")
    # Убираем все двойные пробелы, для корректности split
    pp = "  "
    while pp in str_input:
        str_input = str_input.replace("  ", " ")
    else:
        set_str = set(str_input.split())
    print(len(set_str))


"""Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию)."""


def nod():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    print("НОД равен", num1 + num2)


func_dict = {product_sum: product_sum, largest_word: largest_word,
             excess_symbols: excess_symbols, little_big: little_big,
             fibonacci: fibonacci, palindrome: palindrome, square: square,
             high_low: high_low, camel: camel, xo_check: xo_check,
             num_to_bin: num_to_bin, num_bit: num_bit,
             fizz_and_buzz: fizz_and_buzz, list_practice: list_practice,
             tuple_practice: tuple_practice, pairs: pairs,
             uni_elements: uni_elements, not_null_elements: not_null_elements,
             dict_gen: dict_gen, countries: countries,
             set_different: set_different, set_diff_in_one: set_diff_in_one,
             schoolboy: schoolboy, diff_words_str: diff_words_str, nod: nod}


def runner(*args):
    if not args:
        for item in func_dict:
            func = func_dict[item]
            func()
    else:
        for item in args:
            func = func_dict[item]
            func()
    return args


# runner()
# runner(nod)
runner(nod, fibonacci, pairs, dict_gen, largest_word)
