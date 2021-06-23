"""Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.
The binary number returned should be a string."""

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
_sum = num1 + num2  # Сумма введённых данных
_bin = ""
while _sum > 0:  # Переводим в двоичную систему
    _bin = str(_sum % 2) + _bin
    _sum = _sum // 2

print(_bin)
