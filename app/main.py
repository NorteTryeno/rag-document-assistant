import streamlit as st

from rag.chat import generate_response

from rag.document_loader import load_document

st.set_page_config(
    page_title="RAG DOCUMENT—ASSISTANT",
    layout="wide"
)

#Session_state
if "messages" not in st.session_state:
    st.session_state.messages = []


#Header
st.title("RAG DOCUMENT—ASSISTANT")
st.caption("Chat with your documents using GPT + RAG")

#Sidebar
with st.sidebar:
    st.header("Documents")

    uploaded_files = st.file_uploader(
        "Upload files",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

    st.divider()

    st.write("Supported formats:")
    st.write("— PDF")
    st.write("— TXT")
    st.write("— DOCX")

    st.divider()

    if uploaded_files:
        file = uploaded_files[0]
        st.write(file.name)
        st.write(file.type)
        st.write(load_document(file)[:1000])

#Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

#Chat input
user_input = st.chat_input(
    "Ask something..."
)

if user_input:

    #Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    #Display user message
    with st.chat_message("user"):
        st.write(user_input)

    #Generate asssistant response
    assistant_response = generate_response(
        st.session_state.messages
    )

    #Save assistant response
    st.session_state.messages.append({
        "role":"assistant",
        "content":assistant_response
    })

    #Display assistant response
    with st.chat_message("assistant"):
        st.write(assistant_response)    