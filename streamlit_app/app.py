import sys
import os

# Add project root (parent of this file) to sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from graph.graph_builder import build_graph

# Build the LangGraph graph
graph = build_graph()

# Session state initialization
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("💬 Clinical Trial Matcher")

# Show chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask me anything about clinical trials...")

if prompt:
    # Append user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Track previous length
    prev_len = len(st.session_state["messages"])

    # Invoke the graph
    result = graph.invoke({"messages": st.session_state["messages"]})

    # Get new messages only
    new_messages = result["messages"][prev_len:]

    # Display and store new messages
    for msg in new_messages:
        st.session_state["messages"].append(msg)
        if msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.markdown(msg["content"])
