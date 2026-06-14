from pypdf import PdfReader

# from langchain_community.document_loaders import Docx2txtLoader


def load_document(file):

    if file.type == "application/pdf":
        return load_pdf(file)

    elif file.type == "text/plain":
        return load_txt(file)
    
    # как добавить сюда docx? - Пока что отложим реализацию. все равно переписывать всю связку под langchain
    # elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
    #     return load_docx(file)

    else:
        raise ValueError(
            f"Unsupported file type: {file.type}"
        )


def load_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    file.seek(0)

    return text


# def load_docx(file):

#     loader = Docx2txtLoader(file)
#     documents = loader.load()
    
#     file.seek(0)

#     return documents[0].page_content

def load_txt(file):

    text = file.read().decode("utf-8")

    file.seek(0)

    return text
