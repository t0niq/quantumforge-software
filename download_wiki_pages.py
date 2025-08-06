import os
import csv
import requests
from bs4 import BeautifulSoup
from slugify import slugify

# Папки
RAW_DIR = "raw_pages"
os.makedirs(RAW_DIR, exist_ok=True)

# Файл со списком страниц
CSV_FILE = "pages_list.csv"

# Загрузка CSV
with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row["Название"]
        url = row["URL"]
        print(f"Скачиваем: {title} ({url})")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"Ошибка загрузки {title}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.select_one("div.mw-parser-output")
        if not content:
            print(f"Контент не найден для {title}")
            continue

        # Удаляем таблицы, скрипты, теги aside
        for tag in content(["script", "style", "table", "aside", "figure"]):
            tag.decompose()

        text = content.get_text(separator="\\n", strip=True)

        filename = f"{slugify(title)}.txt"
        filepath = os.path.join(RAW_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Сохранено: {filepath}")
