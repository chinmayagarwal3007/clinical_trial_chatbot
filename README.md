# 🧪 Clinical Trial Matcher Chatbot

This is an AI-powered multi-modal chatbot that helps users find relevant clinical trials, get pharmaceutical info, and engage in small talk. It's built using:

- **Streamlit** – for the frontend UI  
- **LangGraph** – to manage multi-turn conversations and branching logic  
- **Gemini (Google)** – as the LLM  
- **FAISS** – as the vector store for fast semantic search over trial data  

---

## ✅ Features Implemented (as of 2025-05-30)

### 💬 Chatbot Modes
- **Small talk** support (e.g., jokes, greetings)  
- **General pharmaceutical queries**  
- **Clinical Trial Matcher**
  - Users can describe a patient or ask about a condition
  - The system retrieves relevant trials from the FAISS vector store
  - LLM responds using context from the last 4 exchanges (8 messages)

### 🔎 Vector Store: FAISS
- Clinical trial metadata (sampled from real formats) is embedded and stored in FAISS for similarity-based retrieval

### 🧠 Multi-turn Memory
- Last 4 chat rounds (8 messages) are retained for contextual responses

### 📦 Modular Architecture
- Nodes for routing, pharma info, small talk, and clinical trial search implemented using **LangGraph**

### 📊 Streamlit Frontend
- User interacts via a chat interface powered by Streamlit
- Fully working end-to-end chat system

---

## 📁 Folder Structure

.
├── clinical_trials.csv # Sample trial data
├── graph/ # LangGraph nodes and builder
├── llm/ # Gemini-based prompt generation
├── streamlit_app/ # Streamlit frontend app
├── utils/ # FAISS search, embeddings
├── main.py # CLI for testing
└── requirements.txt # Dependencies

---

## 🚀 Upcoming Features

- Session-based chat UI (New Chat, View History)
- PDF upload for patient information extraction
- Persistent chat history across sessions