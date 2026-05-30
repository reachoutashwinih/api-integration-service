from fastapi import FastAPI
from app.services.weather_service import get_weather
from app.services.news_service import get_news

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API Integration Service"}


@app.get("/weather")
def weather(city: str = "bangalore"):
    data = get_weather(city)
    return {"temperature": data.get("temperature")}


@app.get("/dashboard")
def dashboard(city: str = "bangalore"):
    weather = get_weather(city)
    news = get_news(city)
    return {"city": city, "weather": weather, "news": news}