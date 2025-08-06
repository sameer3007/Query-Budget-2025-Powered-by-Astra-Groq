# Query-Budget-2025-Powered-by-Astra-Groq
# 🇮🇳 Budget 2025 Q&A App — Streamlit + Astra DB + LangChain + Groq

This project is a simple **Streamlit web app** that allows users to **ask questions** about the **Union Budget 2025 of India** using data stored in **Astra DB (DataStax Cassandra)**. The app uses **LangChain**, **Groq LLM**, and **HuggingFace embeddings** to retrieve relevant information and generate intelligent responses.

> 🧠 You can ask:  
> - "What is the allocation for education?"  
> - "How much was allocated to infrastructure?"  
> - "What are the key announcements in the budget?"

---

## 💡 Features

- ✅ Query a pre-indexed PDF (Budget 2025) from Astra DB
- ✅ No PDF upload required – data is already embedded
- ✅ Uses `Groq` LLM with `Gemma2-9b-It` model for answers
- ✅ Conversational interface with chat history
- ✅ Option to clear chat session

---

## 📦 Tech Stack

| Tool         | Description                                |
|--------------|--------------------------------------------|
| [Streamlit](https://streamlit.io) | Web app framework for Python          |
| [LangChain](https://www.langchain.com) | Framework for LLM applications       |
| [Groq](https://groq.com/) | Ultra-fast LLM inference (Gemma 2-9b) |
| [CassIO](https://docs.datastax.com/en/astra/docs/develop/cassio/cassio-overview.html) | Astra DB + LangChain integration     |
| [HuggingFace Embeddings](https://huggingface.co) | Used for document vectorization     |
| [Astra DB](https://www.datastax.com/astra) | Vector DB built on Apache Cassandra |

---

