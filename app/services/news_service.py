import httpx
from app.config.settings import settings


async def get_news(city: str):

    url = (
        "https://gnews.io/api/v4/search"
        f"?q={city}"
        f"&lang=en"
        f"&max=5"
        f"&apikey={settings.gnews_api_key}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    articles = data.get("articles", [])

    return [
        {
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
        }
        for article in articles
    ]