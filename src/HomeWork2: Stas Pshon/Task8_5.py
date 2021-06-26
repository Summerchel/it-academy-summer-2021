"""Complete the method/function so that it converts
dash/underscore delimited words into camel casing.
The first word within the output should be capitalized
only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case)."""

_str = input("Введите строку через - или _:")
_list = _str.replace("-", " ").replace("_", " ")  # Заменяем - и _ на пробелы
_list = _list.title()  # Все слова ставим с заглавной буквы
_list = _list.split()  # Делаем список
_str = "".join(_list)  # Соеденяем всю строку
print(_str)
