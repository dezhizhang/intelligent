from sqlalchemy import Column,Integer, String
from src.models.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"