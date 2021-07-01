"""Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников."""

all_lang = set()  # Языки которые знают все школьники
any_lang = set()  # Все языки, которые знают школьники
cur_lang = set()  # Языки текущего ученика, для проверки
n = int(input("Введите количество учеников: "))
for i in range(1, n + 1):
    mi = int(input(f"Сколько языков знает {i}-й ученик? "))
    for y in range(1, mi + 1):
        lang = input(f"Введите {y}-й язык {i}-го ученика ")
        any_lang.add(lang)
        cur_lang.add(lang)
    all_lang = all_lang.intersection(cur_lang) if all_lang else cur_lang
    cur_lang = set()
l_all, l_any = list(all_lang), list(any_lang)
print("Всего языков которые знают все:", len(l_all))
for q in range(len(l_all)):
    print(l_all[q])
print("Всего языков:", len(l_any))
for w in range(len(l_any)):
    print(l_any[w])
