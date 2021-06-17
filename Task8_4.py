"""Write a function that takes an integer as input,
and returns the number of bits that are equal to one in the binary representation of that number.
You can guarantee that input is non-negative."""

_num = int(input("Введите число: "))
_bin = ""
while _num > 0:  # Переводим в двоичную систему
    _bin = str(_num % 2) + _bin
    _num = _num // 2
bit = len(str(_bin))  # Считаем количество бит
print(bit)
