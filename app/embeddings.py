from chromadb.utils import embedding_functions

def get_embedding_function(model_name: str = "all-MiniLM-L6-v2"):
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=model_name
    )