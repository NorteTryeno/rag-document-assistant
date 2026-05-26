from utils.openai_client import client

def generate_response(messages):

    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content
