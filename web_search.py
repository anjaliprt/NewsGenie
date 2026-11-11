from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):

    try:
        result = client.search(query=query, max_results=3)

        if not result["results"]:
            return "No relevant web results found."

        output = "⚠️ News API unavailable.\n\nShowing Web Search Results:\n\n"

        for item in result["results"]:
            output += f"🔹 {item['title']}\n"
            output += f"{item['url']}\n\n"

        return output

    except Exception:
        return "❌ Web Search temporarily unavailable."