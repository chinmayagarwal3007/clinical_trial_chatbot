# graph/nodes.py
from llm.gemini_client import generate_response
from utils.trial_search import search_trials_faiss

def router_node(state):
    user_input = state["messages"][-1]["content"]
    prompt = f"""
Classify the user's message into one of the following categories:
1. small_talk - if the message is casual, unrelated to pharma or clinical trials.
2. pharma_info - if the message is about general pharmaceutical knowledge, drugs, regulations, or diseases.
3. clinical_trial_match - if the user is sharing information about a patient and wants help finding a clinical trial.

Message: "{user_input}"

Respond with only one of: small_talk, pharma_info, or clinical_trial_match.
"""
    response = generate_response(prompt)
    classification = response.strip().lower()
    return classification

def small_talk_node(state):
    user_input = state["messages"][-1]["content"]
    response = generate_response(user_input)
    state["messages"].append({"role": "assistant", "content": response})
    return state

def clinical_trial_node(state):
    user_input = state["messages"][-1]["content"]
    results = search_trials_faiss(user_input)
    trials_text = "\n\n".join([
        f"**{trial['Study Title']}**\n{trial['Brief Summary']}\nURL: {trial['Study URL']}"
        for trial in results
    ])
    prompt = f"The user asked about clinical trials. Here are the relevant ones:\n\n{trials_text}\n\nRespond with a helpful summary."
    response = generate_response(prompt)
    state["messages"].append({"role": "assistant", "content": response})
    return state

def pharma_info_node(state):
    user_input = state["messages"][-1]["content"]
    response = generate_response(user_input)  # Just respond directly
    state["messages"].append({"role": "assistant", "content": response})
    return state

def router(state):
    last_msg = state["messages"][-1]["content"].lower()
    if last_msg == "small_talk":
        return "small_talk"
    elif last_msg == "clinical_trial_match":
        return "clinical_trial_match"
    else:
        return "pharma_info"

def start_node(state):
    return state