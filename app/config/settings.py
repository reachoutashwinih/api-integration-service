from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    weather_api_key: str
    gnews_api_key: str

    model_config = SettingsConfigDict(env_file="properties.env")


settings = Settings()