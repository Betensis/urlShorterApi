from pathlib import Path

from sqlalchemy.engine import make_url, URL
from starlette.config import Config
from starlette.datastructures import Secret

ROOT_DIR = Path(__file__).parent
MODEL_DIRS: list[Path] = [ROOT_DIR / "db" / "models"]

config = Config(ROOT_DIR / ".env")

DEBUG = config("DEBUG", default=False)

DB_DRIVER = config("DB_DRIVER")
DB_HOST = config("DB_HOST", default=None)
DB_PORT = config("DB_PORT", cast=int, default=None)
DB_USER = config("DB_USER", default=None)
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default=None)
DB_DATABASE = config("DB_DATABASE", default=None)
DB_DSN = str(
    config(
        "DB_DSN",
        cast=make_url,
        default=URL(
            drivername=DB_DRIVER,
            username=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE,
        ),
    )
)
# ) if not DEBUG else 'sqlite:///test.db'
