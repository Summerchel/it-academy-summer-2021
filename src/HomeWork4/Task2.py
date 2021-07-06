"""Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится."""

earth = {}
n_num = int(input("Сколько стран будем вводить? "))
for item in range(n_num):
    country_city = input("Введите сначало страну, потом город(а): ")
    country_city = country_city.split()
    cities = country_city[1:]  # Список только городов
    country = country_city[0]
    earth[country] = cities  #
m_num = int(input("Сколько городов будем проверять? "))
list_countries = ""
for index in range(m_num):  # Цикл от 0 до M
    city_find = input("Введите город: ")
    for country_find, in_country in earth.items():
        if city_find in in_country:
            list_countries += country_find
for printed_city in list_countries:
    print(printed_city)
