import httpx
from app.config.settings import settings


CITY_COORDS = {
    "bangalore": (12.97, 77.59),
    "mumbai": (19.07, 72.87),
    "delhi": (28.61, 77.20),
}


async def get_weather(city: str):

    city = city.lower()

    if city not in CITY_COORDS:
        city = "bangalore"

    lat, lon = CITY_COORDS[city]

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&current=temperature_2m"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"]
    }