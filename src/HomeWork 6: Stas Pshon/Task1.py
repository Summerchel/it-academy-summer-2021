"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать
какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д."""


import random


class Tammagotchi(object):
    """Виртуальный зоопарк"""

    def __init__(self, name):
        self.name = name
        self.hunger = random.randrange(0, 10)
        self.boredom = random.randrange(0, 10)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        states = {
            10: "прекрасно",
            20: "неплохо",
            30: "так себе",
            40: "бывало и лучше",
        }
        for state in states:
            if unhappiness <= state:
                mood = states[state]
            else:
                mood = "ужасно"
            return mood

    def talk(self):
        print(f"Меня зовут {self.name} и сейчас я "
              f"чувствую себя {self.mood}" "\n")
        self.__pass_time()

    def eat(self):
        food = random.randrange(0, 10)
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = random.randrange(0, 10)
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    Tamma_name = []
    new_pat = input("Вы хотите создать новую зверушку Yes/No? ")
    while new_pat.lower() == "yes":
        name = input("Как вы назовёте свою зверушку? ")
        Tamma_name.append(name)
        Tamma = Tammagotchi(name)
        new_pat = input("Вы хотите создать новую зверушку Yes/No? ")

    choice = None
    while choice != "0":
        print(
            """
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """
        )
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверушкой
        elif choice == "1":
            Tamma.talk()
        # кормление зверюшки
        elif choice == "2":
            Tamma.eat()
        # игра со зверушкой
        elif choice == "3":
            Tamma.play()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


if __name__ == '__main__':
    main()
