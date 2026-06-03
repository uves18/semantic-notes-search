# 🔍 Semantic Notes Search

A semantic search engine for personal notes using sentence embeddings and vector similarity search. Upload your `.txt` notes and search them using natural language — not just keywords.

## What it does
 Embeds notes using `sentence-transformers` (all-MiniLM-L6-v2)
 Stores and retrieves vectors using ChromaDB
 Returns semantically similar notes ranked by relevance score
 Clean Streamlit interface for uploading and searching

## Stack
Python · ChromaDB · Sentence Transformers · Streamlit

## Project Structure
semantic-notes-search/
├── app/
│   ├── embeddings.py     # embedding model setup
│   ├── vector_store.py   # ChromaDB operations
│   ├── search.py         # search and ranking logic
│   └── ui.py             # Streamlit UI components
├── tests/
│   └── test_search.py
├── main.py
└── requirements.txt

## How to run
```bash
pip install -r requirements.txt
streamlit run main.py
```

Then upload any `.txt` files from the sidebar and search them naturally.