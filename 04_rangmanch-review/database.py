from sqlmodel import SQLModel,Session,create_engine

DATABASE_URL="sqlite:///rangmanch.db"

engine=create_engine(DATABASE_URL,echo=True)


def create_tables():
    """ Create tables defined by SQL Model Class """
    SQLModel.metadata.create_all(engine)


def get_session():
    """ Dependency that provides database session per request """
    with Session(engine) as session:
        yield session

