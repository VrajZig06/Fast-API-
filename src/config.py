# here we make special class that inherits BaseSettings Class that allow us to Read .env File Variables.

from pydantic_settings import BaseSettings,SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

# This Class's Instance give you all Environment Variable Access
class Settings(BaseSettings):
    DATABASE_URL : str
    model_config = SettingsConfigDict(
        env_file="./env",
        extra="ignore" 
    )


# Instance of Settings Class that will Provide all .env Variables
Config = Settings()