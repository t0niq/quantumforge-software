import faiss
import pickle
import os
import sys
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

# Настройки
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EMBED_MODEL_PATH = os.path.join(SCRIPT_DIR, "models/embeddings/all-MiniLM-L6-v2")
LLM_PATH = os.path.join(SCRIPT_DIR, "models/llama/mistral-7b-instruct-v0.2.Q4_K_M.gguf")
FAISS_INDEX_PATH = os.path.join(SCRIPT_DIR, "faiss.index")
METADATA_PATH = os.path.join(SCRIPT_DIR, "metadatas.pkl")
K = 4  # сколько чанков использовать
MAX_TOKENS = 512
FEW_SHOT_EXAMPLES = [
    {
        "q": "Как называется трон, на котором сидит король?",
        "a": "Название трона, на котором сидит король - Почётное кресло губернатора"
    },
    {
        "q": "Как называется тайное общество наёмных убийц",
        "a": "Тайное общество наёмных убийц называется Агенты Сенной линии"
    },
    {
        "q": "Какая столица Франции?",
        "a": "В предоставленном контексте нет информации о столице Франции. Я не знаю."
    },
]

# Загрузка моделей
try:
    print("📦 Загружаем модель эмбеддингов...")
    embedder = SentenceTransformer(EMBED_MODEL_PATH)

    print("📦 Загружаем LLaMA модель...")
    llm = Llama(model_path=LLM_PATH, n_ctx=2048, n_threads=6)

    print("📦 Загружаем FAISS индекс...")
    if not os.path.exists(FAISS_INDEX_PATH):
        raise FileNotFoundError(f"FAISS индекс не найден: {FAISS_INDEX_PATH}")
    if not os.path.exists(METADATA_PATH):
        raise FileNotFoundError(f"Метаданные не найдены: {METADATA_PATH}")
        
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        db = pickle.load(f)
        
    print("✅ Все модели загружены успешно!")
    
except Exception as e:
    print(f"❌ Ошибка при загрузке моделей: {e}")
    sys.exit(1)

def search_context(query, top_k=K):
    try:
        query_vec = embedder.encode([query])
        distances, indices = index.search(query_vec, top_k)
        return [db["documents"][i] for i in indices[0]]
    except Exception as e:
        print(f"❌ Ошибка при поиске контекста: {e}")
        return []

def build_prompt(query, context_chunks):
    context_text = "\n\n".join(context_chunks)
    few_shot = "\n\n".join([f"Q: {ex['q']}\nA: {ex['a']}" for ex in FEW_SHOT_EXAMPLES])

    prompt = f"""Ты помощник, который отвечает ТОЛЬКО на основе предоставленного контекста. Если в контексте нет информации для ответа на вопрос, ты ДОЛЖЕН сказать "Я не знаю" или "В предоставленном контексте нет информации об этом".

ВАЖНО: Не используй свои общие знания. Отвечай только на основе контекста ниже.

{few_shot}

Контекст:
{context_text}

Q: {query}
A:"""
    return prompt

def ask_rag_bot(query):
    try:
        context_chunks = search_context(query)
        if not context_chunks:
            return "Извините, не удалось найти релевантный контекст для вашего вопроса."
            
        prompt = build_prompt(query, context_chunks)
        output = llm(prompt, max_tokens=MAX_TOKENS, stop=["Q:"], echo=False)
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return f"Произошла ошибка при обработке вопроса: {e}"

if __name__ == "__main__":
    print("🧠 Введи вопрос (или 'exit'):")
    while True:
        try:
            query = input("> ")
            if query.lower() in ("exit", "quit"):
                break
            if query.strip():
                answer = ask_rag_bot(query)
                print("\n🤖 Ответ:")
                print(answer)
                print("\n— — — — — — — — —\n")
        except KeyboardInterrupt:
            print("\n\n👋 До свидания!")
            break
        except Exception as e:
            print(f"❌ Ошибка: {e}")

