import streamlit as st

st.set_page_config(
    page_title="RAG DOCUMENT—ASSISTANT",
    layout="wide"
)

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

#Main chat area
st.subheader("Chat")

user_input = st.chat_input("Ask a question about your documents...")

if user_input:
    st.chat_message("user").write(user_input)

    st.chat_message("assistant").write("RAG pipeline is not connected yet.")
