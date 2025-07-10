# 🧠 Business RAG AI Agent

This project is a **fully automated RAG (Retrieval-Augmented Generation)** system designed to:

- Ingest and summarize content from **provided URLs** (blogs, product pages, documentation, etc.)
- Store the information in a **vector database** using semantic embeddings
- Serve a **ChatGPT-style interface** to answer business-related questions using real company data
- Automatically **update knowledge daily** from the same URLs via a CRON job

---

## 📌 Features

- 🔗 Accepts URLs (websites, blogs, help docs)
- 🤖 Uses LLM (like GPT-4) to summarize and chunk data
- 🔍 Vector database (Chroma or Pinecone) for fast retrieval
- 💬 Chatbot interface with contextually accurate answers
- 🔁 Daily auto-refresh of content from URLs (fully automated)
- ⚙️ Built with FastAPI + React (or plain HTML optional)

---

## 🧰 Tech Stack

| Layer         | Tools Used                              |
|---------------|------------------------------------------|
| Backend       | Python, FastAPI                          |
| LLM           | OpenAI GPT-4 (via API)                   |
| Embeddings    | OpenAI `text-embedding-ada-002`          |
| Vector Store  | Chroma (MVP), can switch to Pinecone     |
| Scraping      | BeautifulSoup, newspaper3k, or Readability API |
| Summarization | GPT-4 or GPT-3.5                         |
| Frontend      | React or HTML/CSS/JS (simple chat UI)    |
| Scheduler     | CRON + Python Script                     |

---
