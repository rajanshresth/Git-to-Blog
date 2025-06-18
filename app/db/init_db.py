import os
from sqlalchemy import create_engine
from app.db.models import Base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set.")
engine = create_engine(DATABASE_URL)  # Use sync engine for DDL

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created!")

if __name__ == "__main__":
    create_tables()
