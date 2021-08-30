"""Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors"""


try:
    num = int(input("Input number: "))

except ValueError:
    print("This is not a number. We leave.")


class TooManyErrors(RuntimeError):
    pass


def dec(any_func):
    total_count = 0
    any_func(2)

    def wrapper(count_num):

        nonlocal total_count

        for _ in range(count_num + 1):
            total_count += 1
            try:
                if total_count > count_num:
                    raise TooManyErrors(f'TooManyErrors. {count_num}')
                else:
                    print(f'Done: {total_count}')
            except TooManyErrors as err:
                print(err)

    return wrapper


@dec
def func(x):
    return x ** 2


func(num)
