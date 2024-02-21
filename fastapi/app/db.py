from sqlalchemy import ARRAY, Column, Date, String, UUID, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import settings


Base = declarative_base()

engine = create_engine(settings.postgres_dsn.unicode_string())

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    else:
        if session.is_active:
            session.commit()
    finally:
        session.close()


class Person(Base):
    __tablename__ = 'person'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    apelido = Column(String(32), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    nascimento = Column(Date, nullable=False)
    stack = Column(ARRAY(String(32)))
