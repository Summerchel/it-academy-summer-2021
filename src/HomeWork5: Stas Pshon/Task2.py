"""Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)"""


def cache(any_func):
    """Кэш предыдущих вызовов функций"""

    def wrapper(*args, **kwargs):
        result = any_func(*args, **kwargs)
        with open("cache.txt", "r") as reading:
            text = reading.readline()
            print("Прошлые результаты: ", text)
        with open("cache.txt", "w") as writing:
            writing.write(str(text))
            writing.write(", ")
            writing.write(str(result))
            print("Сейчас функция равна: ", result)

        return result

    return wrapper


@cache
def func(x, y):
    return x + y


func = cache(func(2, 7))
