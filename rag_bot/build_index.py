import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

EMBED_MODEL_PATH = "models/embeddings/all-MiniLM-L6-v2"
DATA_DIR = "data"
CHUNK_SIZE = 500  # символов
CHUNK_OVERLAP = 100

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# Загрузка модели
print("🔍 Загружаем модель эмбеддингов...")
model = SentenceTransformer(EMBED_MODEL_PATH)

documents = []
metadatas = []

print("📖 Загружаем тексты...")
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
            text = f.read()
            for chunk in chunk_text(text):
                documents.append(chunk)
                metadatas.append({"source": filename})

print(f"🧠 Всего чанков: {len(documents)}")

# Генерация эмбеддингов
print("🔧 Генерация эмбеддингов...")
embeddings = model.encode(documents, show_progress_bar=True, convert_to_numpy=True)

# Создание и сохранение FAISS индекса
print("💾 Создание и сохранение FAISS индекса...")
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "faiss.index")
with open("metadatas.pkl", "wb") as f:
    pickle.dump({"documents": documents, "metadatas": metadatas}, f)

print("✅ Индекс создан и сохранён.")

