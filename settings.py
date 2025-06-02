from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env" 