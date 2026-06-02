import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from app.services.weather_service import get_weather
from app.services.news_service import get_news
from datetime import datetime
from app.models.dashboard import DashboardResponse
from app.auth.routes import router as auth_router
from fastapi import Depends
from app.auth.dependencies import get_current_user

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Configure OpenAPI security scheme for Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="API Integration Service",
        version="1.0.0",
        description="API with authentication and dashboard",
        routes=app.routes,
    )
    
    openapi_schema["components"]["securitySchemes"] = {
        "Bearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "JWT token from /auth/login endpoint"
        }
    }
    
    openapi_schema["security"] = [{"Bearer": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


@app.get("/")
def home():
    return {"message": "API Integration Service"}


@app.get("/weather")
def weather(city: str = "bangalore"):
    return {"message": "Please use async weather endpoint"}


@app.get("/dashboard")
async def dashboard(city: str = "bangalore", user: str = Depends(get_current_user)):

    weather_task = get_weather(city)
    news_task = get_news(city)

    weather, news = await asyncio.gather(weather_task, news_task)

    return {
        "success": True,
        "user": user,
        "city": city,
        "weather": weather,
        "news_count": len(news),
        "news": news
    }