"""Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. The string can contain any char."""

_str = input("Введите строку: ")
_x = 0  # Счётчик Х
_o = 0  # Счётчик О
for i in _str:
    if "x" == i or "X" == i:   # Является ли символ Х
        _x += 1
    elif "o" == i or "O" == i:  # Является ли символ О
        _o += 1
if _x == _o:  # Сравнение Х и О
    print("True")
