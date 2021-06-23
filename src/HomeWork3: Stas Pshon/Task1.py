"""Напишите программу, которая печатает цифры от 1 до 100,
 но вместо чисел, кратных 3 пишет Fizz,
 вместо чисел кратный 5 пишет Buzz,
 а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""

FizzBuzz = 1
while FizzBuzz <= 100:
    if FizzBuzz % 15 == 0:
        print("FizzBuzz")
    elif FizzBuzz % 3 == 0:
        print("Fizz")
    elif FizzBuzz % 5 == 0:
        print("Buzz")
    else:
        print(FizzBuzz)
    FizzBuzz += 1
