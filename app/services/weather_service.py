import requests


CITY_COORDS = {
    "bangalore": (12.97, 77.59),
    "mumbai": (19.07, 72.87),
    "delhi": (28.61, 77.20),
}


def get_weather(city: str):

    city = city.lower()

    if city not in CITY_COORDS:
        city = "bangalore"

    lat, lon = CITY_COORDS[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m"
    )

    response = requests.get(url)

    data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"]
    }