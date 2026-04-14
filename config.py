import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))