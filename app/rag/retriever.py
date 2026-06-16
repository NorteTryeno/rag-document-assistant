from langchain_core.documents import Document

def retrieve_documents(vector_store, query, k=4) -> list[Document]:
    
    return vector_store.similarity_search(query, k=k)