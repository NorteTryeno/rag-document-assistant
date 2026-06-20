import streamlit as st

from rag.chat import generate_response
from rag.document_processor import create_documents
from rag.document_splitter import split_documents
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_documents

st.set_page_config(
    page_title="RAG DOCUMENT—ASSISTANT",
    layout="wide"
)

#Session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = []

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None  

if "retrieved_documents" not in st.session_state:
    st.session_state.retrieved_documents = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

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

    current_files = [
        (file.name, file.size)
        for file in uploaded_files
    ]

    st.divider()

    st.write("Supported formats:")
    st.write("— PDF")
    st.write("— TXT")
    st.write("— DOCX")

    st.divider()

    if uploaded_files and current_files != st.session_state.processed_files:
        documents = create_documents(uploaded_files)
        chunks = split_documents(documents)

        st.session_state.documents = documents
        st.session_state.chunks = chunks
        st.session_state.vector_store = create_vector_store(st.session_state.chunks)
        st.session_state.retrieved_documents = []
        st.session_state.processed_files = current_files

    elif not uploaded_files:
        st.session_state.documents = []
        st.session_state.chunks = []
        st.session_state.vector_store = None
        st.session_state.retrieved_documents = []
        st.session_state.processed_files = []

    st.write("Documents:", len(st.session_state.documents))
    st.write("Chunks:", len(st.session_state.chunks))   

    if st.session_state.retrieved_documents:
        with st.expander("retrieved chunks"):
            st.write("Found:", len(st.session_state.retrieved_documents))
            for doc in st.session_state.retrieved_documents:
                st.write(doc.metadata)
                st.write(doc.page_content[:300])


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

    if st.session_state.vector_store is not None:
        st.session_state.retrieved_documents = retrieve_documents(
            st.session_state.vector_store,
            user_input,
        )
    else:
        st.session_state.retrieved_documents = []       


    if st.session_state.vector_store is None:
        assistant_response = (
            "Загрузите документ, прежде чем задавать вопрос."
        )

    elif not st.session_state.retrieved_documents:
        assistant_response = (
            "Не удалось найти подходящий контекст. "
            "Попробуйте переформулировать вопрос."
        )    

    else:
        #Generate asssistant response
        assistant_response = generate_response(
            st.session_state.messages,
            st.session_state.retrieved_documents
        )

    #Save assistant response
    st.session_state.messages.append({
        "role":"assistant",
        "content":assistant_response
    })

    #Display assistant response
    with st.chat_message("assistant"):
        st.write(assistant_response)
