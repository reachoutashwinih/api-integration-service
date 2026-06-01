# API Integration Service

Lightweight FastAPI service that aggregates weather and news for a requested city.

Features
- Fetch current temperature for supported cities using OpenWeather.
- Fetch recent news articles for a city using GNews.
- Simple `/weather` and `/dashboard` endpoints for integration and testing.

Quick Start

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your API keys in `properties.env` (repo root):

```
gnews_api_key="your_gnews_api_key_here"
weather_api_key="your_openweather_api_key_here"
```

4. Run the app with Uvicorn:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Endpoints
- `GET /` — health/info message.
- `GET /weather?city=<city>` — returns `{ "temperature": <value> }` for supported cities.
- `GET /dashboard?city=<city>` — returns combined JSON: `{ "city": "...", "weather": {...}, "news": [...] }`.

Notes
- Supported cities (case-insensitive): `bangalore`, `mumbai`, `delhi`. Unknown cities default to `bangalore` for weather.
- `properties.env` is loaded by `config/settings.py`. You can also export `gnews_api_key` and `weather_api_key` in your shell.
- If `/weather` returns 401 or fails, check that `weather_api_key` is present and valid for OpenWeather.

Development
- The code lives in `app/services` and `app/main.py`.
- To run quick local checks without starting the server, you can run short scripts that import `get_weather` and `get_news`.

License
- MIT (or choose your preferred license)

If you want, I can add a unit test for the news/ weather services or improve error handling for missing API keys.
