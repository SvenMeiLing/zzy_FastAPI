from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core.config import settings
# from FastAPI.FastAPI_NO_38.all.backend.app.app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, engine=engine)

