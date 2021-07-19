"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов."""

from collections import Counter

try:
    with open("ratings.list", "r") as rl:
        gist_years = []
        gist_level = []
        top250_list = []

        lines = rl.readlines()[28:789451]
        lines_top250 = lines[0:250]
        lines = lines[268:]

        # Гистограмма годов
        for line in lines:
            index = line.find("(")
            god = line[index + 1:index + 5]
            if god.isdecimal() == 1:
                gist_years.append(god)

        # Гистограмма рейтингов
        for line in lines:
            line = line[25::]
            index = line.find(".")
            level = line[index - 1:index + 2]
            gist_level.append(level)

        # Топ 250
        for line in lines_top250:
            index_start = line.find(".")
            index_end = line.find("(")
            top250_list.append(line[index_start + 4:index_end - 1])


except FileNotFoundError:
    print("Данный файл не найден")

with open("top250_movies.txt", "w") as top250:
    for film in top250_list:
        top250.write(film + "\n")
with open("ratings.txt", "w") as rating:
    for level, count in Counter(gist_level).items():
        rating.write(f"{count} фильм(ов) с рейтингом {level}\n")
with open("years.txt", "w") as years:
    for year, count in Counter(gist_years).items():
        years.write(f"В {year} году вышло {count} фильм(ов)\n")
