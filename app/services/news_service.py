import requests
from config.settings import settings

def get_news(city: str):

    url = (
    f"https://gnews.io/api/v4/search"
    f"?q={city}"
    f"&lang=en"
    f"&max=5"
    f"&apikey={settings.gnews_api_key}"
)

    response = requests.get(url)
    response.raise_for_status()

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