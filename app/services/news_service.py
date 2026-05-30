import os
import requests
from dotenv import load_dotenv

# Ensure we load the project's properties.env in the repo root
dotenv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "properties.env")
)
load_dotenv(dotenv_path)

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")


def get_news(city: str):

    url = (
        f"https://gnews.io/api/v4/search"
        f"?q={city}"
        f"&lang=en"
        f"&max=5"
        f"&apikey={GNEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])

    return [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        }
        for article in articles
    ]