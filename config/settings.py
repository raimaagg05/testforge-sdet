import os

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:5000")
API_URL = f"{BASE_URL}/api"
DB_PATH = os.getenv("DB_PATH", "testforge.db")
