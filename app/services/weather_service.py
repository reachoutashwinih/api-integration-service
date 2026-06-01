import requests
from config.settings import settings


def get_weather(city: str):
    if not settings.weather_api_key:
        raise ValueError("Missing OpenWeather API key. Set weather_api_key in properties.env or export it as an environment variable.")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={settings.weather_api_key}"
        "&units=metric"
    )

    response = requests.get(url, timeout=10)
    if response.status_code == 401:
        raise ValueError("Unauthorized OpenWeather API key. Verify weather_api_key in properties.env and ensure the key is active.")
    response.raise_for_status()

    data = response.json()

    return {
        "temperature": data["main"]["temp"]
    }