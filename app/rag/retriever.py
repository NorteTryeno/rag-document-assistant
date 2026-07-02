from langchain_core.documents import Document

RETRIEVAL_TOP_K = 4
MAX_DISTANCE = 1.6


def retrieve_documents(vector_store, query, k=RETRIEVAL_TOP_K, threshold=MAX_DISTANCE) -> list[tuple[Document, float]]:
    scored_documents = vector_store.similarity_search_with_score(
        query,
        k=k
    )
    return [
        (doc, distance)
        for doc, distance in scored_documents
        if distance <= threshold
    ]
