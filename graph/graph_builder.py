# graph/graph_builder.py
from langgraph.graph import StateGraph, END
from .nodes import (
    small_talk_node,
    clinical_trial_node,
    pharma_info_node,
    router,
    start_node
)
from typing import TypedDict, List, Dict, Any



# Define the state schema
class ChatState(TypedDict):
    messages: List[Dict[str, Any]]

def build_graph():
    graph = StateGraph(ChatState)

    # Add all nodes
    graph.add_node("start", start_node)
    #graph.add_node("router", router)
    graph.add_node("small_talk", small_talk_node)
    graph.add_node("pharma_info", pharma_info_node)
    graph.add_node("clinical_trial_match", clinical_trial_node)

    # Set entry point
    graph.set_entry_point("start")

    # Use conditional branching from router
    graph.add_conditional_edges(
        "start",
        router   
    )

    # Each path ends after generating a response
    graph.add_edge("small_talk", END)
    graph.add_edge("pharma_info", END)
    graph.add_edge("clinical_trial_match", END)

    return graph.compile()

