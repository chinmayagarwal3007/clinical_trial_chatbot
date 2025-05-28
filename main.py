# main.py
from graph.graph_builder import build_graph

# Compile the graph
graph = build_graph()

# Initialize conversation state
state = {
    "messages": []
}

print("🔬 Clinical Trial Matcher Chatbot (Type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Add user message to state
    state["messages"].append({"role": "user", "content": user_input})

    # Run graph on current state
    state = graph.invoke(state)

    # Get latest assistant response
    assistant_msg = state["messages"][-1]["content"]
    print(f"\n🤖 Bot: {assistant_msg}\n")
