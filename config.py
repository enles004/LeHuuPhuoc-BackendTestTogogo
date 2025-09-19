import os

from dotenv import load_dotenv

load_dotenv()

# db
pos_db = os.getenv("POSTGRES_URL")
