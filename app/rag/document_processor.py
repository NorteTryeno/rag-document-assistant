from langchain_core.documents import Document
from rag.document_loader import load_document


def create_documents(files):
    documents = []

    for file in files:
        text = load_document(file)

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source":file.name,
                    "file_type":file.type,
                    "size":file.size,
                }
            )
        )
    return documents    