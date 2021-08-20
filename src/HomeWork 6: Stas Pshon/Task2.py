"""Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors"""


class TooManyErrors(RuntimeError):
    pass


def dec(func):
    total_count = 0

    def wrapper(num):

        nonlocal total_count
        for _ in range(num + 1):
            total_count += 1
            try:
                if total_count > num:
                    raise TooManyErrors(f'TooManyErrors. {num}')
                else:
                    print(f'выполнено: {total_count}')
            except TooManyErrors as err:
                print(err)

    return wrapper


@dec
def func(x):
    pass


num = int(input("Введите цифру: "))
func(num)
