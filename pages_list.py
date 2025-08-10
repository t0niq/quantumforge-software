import csv

# Список сущностей по категориям с URL
pages = [
    # Персонажи
    ("Джон Сноу", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Джон_Сноу"),
    ("Дейенерис Таргариен", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Дейенерис_Таргариен"),
    ("Арья Старк", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Арья_Старк"),
    ("Эддард Старк", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Эддард_Старк"),
    ("Серсея Ланнистер", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Серсея_Ланнистер"),
    ("Джейме Ланнистер", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Джейме_Ланнистер"),
    ("Тирион Ланнистер", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Тирион_Ланнистер"),
    ("Станнис Баратеон", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Станнис_Баратеон"),
    ("Петир Бейлиш", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Петир_Бейлиш"),
    ("Бран Старк", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Бран_Старк"),
    ("Сэмвелл Тарли", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Сэмвелл_Тарли"),
    ("Бриенна Тарт", "Персонаж", "https://gameofthrones.fandom.com/ru/wiki/Бриенна_Тарт"),

    # Локации
    ("Винтерфелл", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Винтерфелл"),
    ("Королевская Гавань", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Королевская_Гавань"),
    ("Стена", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Стена"),
    ("Браавос", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Браавос"),
    ("Пайк", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Пайк"),
    ("Чёрный Замок", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Чёрный_Замок"),
    ("Драконий Камень", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Драконий_Камень"),
    ("Хайгарден", "Локация", "https://gameofthrones.fandom.com/ru/wiki/Хайгарден"),

    # Дома
    ("Дом Старков", "Дом", "https://gameofthrones.fandom.com/ru/wiki/Дом_Старков"),
    ("Дом Ланнистеров", "Дом", "https://gameofthrones.fandom.com/ru/wiki/Дом_Ланнистеров"),
    ("Дом Таргариенов", "Дом", "https://gameofthrones.fandom.com/ru/wiki/Дом_Таргариенов"),
    ("Дом Баратеонов", "Дом", "https://gameofthrones.fandom.com/ru/wiki/Дом_Баратеонов"),
    ("Дом Грейджоев", "Дом", "https://gameofthrones.fandom.com/ru/wiki/Дом_Грейджоев"),

    # События
    ("Красная свадьба", "Событие", "https://gameofthrones.fandom.com/ru/wiki/Красная_свадьба"),
    ("Битва Бастардов", "Событие", "https://gameofthrones.fandom.com/ru/wiki/Битва_Бастардов"),
    ("Война Пяти Королей", "Событие", "https://gameofthrones.fandom.com/ru/wiki/Война_Пяти_Королей"),
    ("Великая война", "Событие", "https://gameofthrones.fandom.com/ru/wiki/Великая_война"),
    ("Битва за Королевскую Гавань", "Событие", "https://gameofthrones.fandom.com/ru/wiki/Битва_за_Королевскую_Гавань"),

    # Организации
    ("Ночной Дозор", "Организация", "https://gameofthrones.fandom.com/ru/wiki/Ночной_Дозор"),
    ("Безликие", "Организация", "https://gameofthrones.fandom.com/ru/wiki/Безликие"),
    ("Вера в Семерых", "Организация", "https://gameofthrones.fandom.com/ru/wiki/Вера_в_Семерых"),

    # Артефакты
    ("Железный Трон", "Артефакт", "https://gameofthrones.fandom.com/ru/wiki/Железный_Трон"),
    ("Валирийская сталь", "Артефакт", "https://gameofthrones.fandom.com/ru/wiki/Валирийская_сталь"),
    ("Драконы", "Артефакт", "https://gameofthrones.fandom.com/ru/wiki/Драконы")
]

# Сохраняем в CSV
csv_path = "pages_list.csv"
with open(csv_path, "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Название", "Тип", "URL"])
    writer.writerows(pages)

csv_path