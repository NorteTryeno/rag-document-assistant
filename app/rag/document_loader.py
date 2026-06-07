from pypdf import PdfReader


def load_document(file):

    if file.type == "application/pdf":
        return load_pdf(file)

    elif file.type == "text/plain":
        return load_txt(file)

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


def load_txt(file):

    text = file.read().decode("utf-8")

    file.seek(0)

    return text