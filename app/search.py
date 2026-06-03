def search_notes(collection, query: str, n_results: int = 5) -> list[dict]:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    if not results['documents'][0]:
        return []

    output = []
    for doc, metadata, distance in zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    ):
        output.append({
            'content': doc,
            'filename': metadata['filename'],
            'relevance': (1 - distance) * 100
        })

    return output