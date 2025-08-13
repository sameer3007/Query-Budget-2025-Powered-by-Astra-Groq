import os
import streamlit as st
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import cassio

# ----------------- Environment Setup -----------------
# Set your environment variables or load them via dotenv
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ----------------- Astra DB Init -----------------
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN,
             database_id= ASTRA_DB_ID)

# ----------------- Load Embedding Model & LLM -----------------
embedding = HuggingFaceEmbeddings()
llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)

# ----------------- Connect to Existing Vector DB -----------------
astra_vector_store = Cassandra(
    embedding=embedding,
    table_name="budget_QnA_mini_demo",  # Your existing table with Budget 2025 data
    session=None,
    keyspace=None
)

astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="INDIA Ask Budget 2025", layout="wide")
st.title("📊 Query Budget 2025 — Powered by Astra & Groq")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar with clear chat option
with st.sidebar:
    st.header("🧹 Options")
    if st.button("Clear Chat"):
        st.session_state.chat_history = []

# Input box for question
query = st.text_input("💬 Ask a question about India's Budget 2025:")

# When query is entered
if query:
    with st.spinner("Generating answer..."):
        response = astra_vector_index.query(query, llm=llm)
        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("AI", response))
        st.success("Answer ready!")

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")

