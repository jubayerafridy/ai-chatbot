from app.db.base import Base
from app.db.engine import engine

# Import all models so they are registered
import app.models


def create_tables():
    Base.metadata.create_all(bind=engine)