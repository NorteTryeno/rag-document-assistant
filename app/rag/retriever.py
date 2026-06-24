from langchain_core.documents import Document

RETRIEVAL_TOP_K = 4
RETRIEVAL_THRESHOLD = 0.5

def retrieve_documents(vector_store, query, k=RETRIEVAL_TOP_K, threshold=RETRIEVAL_THRESHOLD) -> list[tuple[Document, float]]:
    scored_documents = vector_store.similarity_search_with_relevance_scores(
        query,
        k=k
    )
    return [
        (doc, score)
        for doc, score in scored_documents
        if score >= threshold
    ]