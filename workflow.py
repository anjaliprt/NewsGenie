from typing import TypedDict
from langgraph.graph import StateGraph, END
from llm import ask_llm
from news_api import get_news
from web_search import web_search


# ---------------- STATE ----------------
class State(TypedDict):
    query: str
    query_type: str
    response: any   # IMPORTANT: can be list or string


# ---------------- 1. LLM CLASSIFIER ----------------
def classify_node(state):
    query = state["query"]

    prompt = f"""
Classify query into:
- news
- general

Query: {query}
Return only one word.
"""

    category = ask_llm(prompt)

    # Gemini failed
    if not category:
        category = "general"
    else:
        category = category.lower().strip()

    # safety fallback
    if category not in ["news", "general"]:
        category = "general"

    return {
        **state,
        "query_type": category
    }


# ---------------- 2. CHATBOT NODE ----------------
def chatbot(state):
    query = state["query"]

    prompt = f"""
You are NewsGenie, an AI assistant.

Answer the following question in a concise manner.

Guidelines:
- Keep the answer within 80-120 words.
- Use simple language.
- Include only the most important information.
- If appropriate, use bullet points (maximum 4).
- Do not add unnecessary introductions or conclusions.

Question:
{query}
"""

    answer = ask_llm(prompt)

    if not answer:
        answer = web_search(query)

    return {
        **state,
        "response": answer
    }

# ---------------- 3. NEWS NODE ----------------
def news(state): 
    news_data = get_news(state["query"]) 
    
    if not news_data: # fallback to web search 
        fallback = web_search(state["query"]) 
        return {**state, "response": fallback} 
    return {**state, "response": news_data}

# ---------------- GRAPH BUILD ----------------
builder = StateGraph(State)

builder.add_node("classifier", classify_node)
builder.add_node("chatbot", chatbot)
builder.add_node("news", news)

# ENTRY POINT
builder.set_entry_point("classifier")


# ---------------- ROUTING ----------------
builder.add_conditional_edges(
    "classifier",
    lambda state: state["query_type"],
    {
        "news": "news",
        "general": "chatbot"
    }
)


builder.add_edge("chatbot", END)
builder.add_edge("news", END)

graph = builder.compile()