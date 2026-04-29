import pytest
from database import engine
from database import SessionLocal
from database import engine, Base


@pytest.fixture()
def db_session():
    """Fixture to connect to DB"""
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


