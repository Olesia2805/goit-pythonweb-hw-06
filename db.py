from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/university"

engine = create_engine(DB_URL)
session = Session(engine)
