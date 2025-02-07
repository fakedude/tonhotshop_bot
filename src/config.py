# type: ignore
from decouple import config
from dotenv import load_dotenv

load_dotenv()

API_ID: int = config('API_ID', cast=int, default=0)
API_HASH: str = config('API_HASH', cast=str, default="")
BOT_TOKEN: str = config('BOT_TOKEN', cast=str, default="")
CHANNEL: str = config('CHANNEL', cast=str, default="")
STREAM_URL: str = config('STREAM_URL', cast=str, default="")
BACKGROUND: str = config('BACKGROUND', cast=str, default="")
NAME: str = config('NAME', cast=str, default="")
SESSION_STRING: str = config('SESSION_STRING', cast=str, default="")
MAX_CONCURRENT_TRANSMISSIONS: int = config('MAX_CONCURRENT_TRANSMISSIONS', cast=int, default=2)
LOG_LEVEL: str = config('LOG_LEVEL', cast=str, default="info")
