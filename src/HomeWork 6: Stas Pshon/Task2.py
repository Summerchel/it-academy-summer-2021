"""Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors"""


try:
    numb = int(input("Input number: "))

except ValueError:
    print("This is not a number. We leave.")


class TooManyErrors(RuntimeError):
    pass


def dec(dec_param):
    def decorator(any_func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            try:
                if count < dec_param:
                    count = count + 1
                    return any_func(*args, **kwargs)
                else:
                    raise TooManyErrors("Permissible amount exceeded "
                                        "program launches")
            except TooManyErrors as errors:
                return errors
            except TypeError:
                return "Data error"
        return wrapper
    return decorator


@dec(numb)
def func(x):
    return x ** 2


print(func(1))
print(func(2))
print(func(3))
print(func(4))
print(func(5))
print(func(6))
print(func(7))
print(func(8))
print(func(9))
print(func(10))
print(func(11))
print(func(12))
print(func(13))
print(func(14))
print(func(15))
