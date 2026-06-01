import asyncio
from fastapi import FastAPI
from app.services.weather_service import get_weather
from app.services.news_service import get_news
from datetime import datetime
from fastapi import HTTPException

from models.dashboard import DashboardResponse

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API Integration Service"}


@app.get("/weather")
def weather(city: str = "bangalore"):
    data = get_weather(city)
    return {"temperature": data.get("temperature")}


@app.get(
    "/dashboard",
    response_model= DashboardResponse
)
async def dashboard(city: str = "bangalore"):
    try:
        weather_task = asyncio.to_thread(get_weather, city)
        news_task = asyncio.to_thread(get_news, city)

        weather, news = await asyncio.gather(
            weather_task,
            news_task
        )
    
        return {
            "success": True,
            "generated_at": datetime.utcnow().isoformat(),
            "city": city,
            "weather": weather,
            "news_count": len(news),
            "news": news
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )