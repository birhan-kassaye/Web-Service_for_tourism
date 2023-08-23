from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
DB_URI = "mysql://username:password@localhost/dbname"
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    def save_to_db(self):
        session = Session()
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session = Session()
        session.delete(self)
        session.commit()
