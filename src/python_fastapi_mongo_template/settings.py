import os

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://mongo:mongo@localhost/")
DEFAULT_DATABASE = os.getenv("DEFAULT_DATABASE", "python_fastapi_mongo_template")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
