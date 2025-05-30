# graph/nodes.py
from llm.gemini_client import generate_response
from utils.trial_search import search_trials_faiss

def router_node(state):
    user_input = state["messages"][-1]["content"].strip()
    prompt = f"""
Classify the user's message into one of the following categories:
1. small_talk - if the message is casual, unrelated to pharma or clinical trials.
2. pharma_info - if the message is about general pharmaceutical knowledge, drugs, regulations, or diseases.
3. clinical_trial_match - if the user is sharing information about a patient and wants help finding a clinical trial.

Message: "{user_input}"

Respond with only one of: small_talk, pharma_info, or clinical_trial_match.
"""
    response = generate_response(prompt)
    state["messages"].insert(0, {"role": "tool", "content": response})
    return state

def small_talk_node(state):
    #user_input = state["messages"][-1]["content"].strip() # Debugging line to check the user input
    messages = state["messages"]
    # Keep only the last 8 messages (4 rounds of user + assistant)
    recent_messages = messages[-8:] if len(messages) > 8 else messages
    # Format messages for Gemini
    chat_history = [{"role": m["role"], "content": m["content"]} for m in recent_messages]
    prompt = f"Continue the conversation based on the following messages:\n\n{chat_history}\n\nRespond with a friendly and engaging message."
    response = generate_response(prompt)
    state["messages"].append({"role": "assistant", "content": response})
    return state

def clinical_trial_node(state):
    user_input = state["messages"][-1]["content"].strip()
    messages = state["messages"]

    # Search vector DB with the user query
    results = search_trials_faiss(user_input)

    # Retain last 8 messages (4 user-assistant exchanges)
    recent_messages = messages[-8:] if len(messages) > 8 else messages
    chat_history_text = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in recent_messages]
    )
    # Prepare clinical trial results text
    if results:
        trials_text = "\n".join([
            f"- **{trial['Study Title']}**: {trial['Brief Summary']} (Age: {trial['Age']})"
            for trial in results
        ])
    else:
        trials_text = "No matching clinical trials found."

    # Merge both prompts
    final_prompt = f"""
You are a helpful medical assistant.

Here is the recent conversation history:
{chat_history_text}

The user is now asking about clinical trials. Based on the query, here are some relevant trial results:

{trials_text}

Continue the conversation helpfully based on the context and the search results.
""".strip()
    # Generate response
    response = generate_response(final_prompt)
    messages.append({"role": "assistant", "content": response})
    return {"messages": messages}


def pharma_info_node(state):
    #user_input = state["messages"][-1]["content"].strip()
    messages = state["messages"]
    # Keep only the last 8 messages (4 rounds of user + assistant)
    recent_messages = messages[-8:] if len(messages) > 8 else messages
    # Format messages for Gemini
    chat_history = [{"role": m["role"], "content": m["content"]} for m in recent_messages]
    prompt = f"Continue the conversation based on the following messages:\n\n{chat_history}\n\nRespond with accurate pharmaceutical information."
    response = generate_response(prompt)  # Just respond directly
    state["messages"].append({"role": "assistant", "content": response})
    return state

def router(state):
    last_msg = state["messages"][0]["content"].lower().strip() 
    if last_msg == "small_talk":
        return "small_talk"
    elif last_msg == "clinical_trial_match":
        return "clinical_trial_match"
    else:
        return "pharma_info"

def start_node(state):
    return state