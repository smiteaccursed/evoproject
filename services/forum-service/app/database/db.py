from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

schema="forum"
class Database_Initializer:
    def __init__(self, base):
        self.base = base

    def init_db(self, postgre_dsn):
        engine = create_engine(postgre_dsn)
        with engine.connect() as connection:
            if not inspect(connection).has_schema(schema):
                connection.execute(CreateSchema(schema))
                connection.commit()
        self.base.metadata.create_all(bind=engine)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return SessionLocal

Base: DeclarativeMeta = declarative_base()
DB_INITIALIZER = Database_Initializer(Base)
