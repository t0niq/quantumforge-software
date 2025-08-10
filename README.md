### 📚 Индексация базы знаний по вымышленному миру (на основе Game of Thrones)

- 📦 Модель эмбеддингов: `all-MiniLM-L6-v2`  
  - Размер эмбеддинга: 384
  - [Модель в Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- 🗂 Использовано файлов: 30
- 🔠 Кол-во чанков: ~60
- ⏱ Время индексации: 90 секунд
- 📁 Содержимое:
  - `got_faiss.index` — FAISS индекс
  - `got_metadata.pkl` — метаданные
  - `build_index.py` — скрипт для генерации индекса
  - `query.py` — скрипт для запроса к индексу

### RAG bot находится в папке rag_bot