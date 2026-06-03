from app.search import search_notes

def test_search_returns_list():
    # smoke test: search on empty collection returns empty list
    import chromadb
    from app.embeddings import get_embedding_function

    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="test_collection",
        embedding_function=get_embedding_function()
    )
    results = search_notes(collection, "test query")
    assert isinstance(results, list)