import chromadb
from app.embeddings import get_embedding_function

def get_collection(collection_name: str = "notes_search"):
    client = chromadb.Client()
    embedding_function = get_embedding_function()
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function
    )

def add_notes(collection, documents: list, ids: list, metadatas: list):
    # Remove existing docs with same IDs to avoid duplicates
    try:
        collection.delete(ids=ids)
    except:
        pass
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )