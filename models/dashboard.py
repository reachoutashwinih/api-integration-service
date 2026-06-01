from pydantic import BaseModel
from typing import List, Dict

class NewsItem(BaseModel):
    title: str
    description: str
    url: str

class DashboardResponse(BaseModel):
    success: bool
    city: str
    weather: Dict
    news_count: int
    news: List[NewsItem]