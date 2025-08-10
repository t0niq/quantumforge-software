from sentence_transformers import SentenceTransformer
import os

model_name = "sentence-transformers/all-MiniLM-L6-v2"
target_folder = "models/embeddings/all-MiniLM-L6-v2"

print(f"📦 Загружаем модель {model_name}...")

model = SentenceTransformer(model_name)

# Сохраняем модель в локальную папку
print(f"💾 Сохраняем модель в {target_folder}...")
model.save(target_folder)

print("✅ Модель успешно загружена и сохранена локально.")

