import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news(topic):
    if not NEWS_API_KEY:
        return []

    try:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={topic}&"
            f"sortBy=publishedAt&"
            f"language=en&"
            f"pageSize=5&"
            f"apiKey={NEWS_API_KEY}"
        )

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        articles = data.get("articles", [])

        news = []
        for article in articles[:5]:
            news.append({
                "title": article.get("title", "No Title"),
                "summary": article.get("description", "No summary available"),
                "url": article.get("url", "")
            })

        return news

    except Exception:
        return []