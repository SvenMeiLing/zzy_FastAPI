import logging
import sys

from app.db.init_db import init_db
from app.db.session import SessionLocal

sys.path.append(r'C:\Users\zouxi\PycharmProject\zzy_FastAPI\FastAPI_NO_38\all\backend\app')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
