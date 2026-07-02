from utils.openai_client import client


def generate_response(question, retrieved_documents):
    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    system_message = {
        "role": "system",
        "content": f"""
        Answer using only the provided context.
        Carefully review all provided context fragments.
        Account for abbreviations, synonyms, and semantically similar phrasing.
        Use the predefined fallback response only after checking the entire context.
        If the context does not contain enough information to answer,
        respond: "В загруженных документах нет информации по этому вопросу."
        """
    }

    user_message = {
        "role": "user",
        "content": f"""
        Context:
        {context}

        Question:
        {question}
        """
    }

    model_messages = [system_message, user_message]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=model_messages,
        temperature=0,
    )

    return response.choices[0].message.content
