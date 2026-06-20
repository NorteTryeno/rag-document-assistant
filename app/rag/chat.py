from utils.openai_client import client


def generate_response(messages, retrieved_documents):
    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    system_message = {
        "role":"system",
        "content": f"""
        Answer using only the provided context.
        If the context does not contain enough information to answer,
        respond: "В загруженных документах нет информации по этому вопросу."
        
        Context:
        {context}
        """
    }

    model_messages = [system_message] + messages

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=model_messages
    )

    return response.choices[0].message.content
