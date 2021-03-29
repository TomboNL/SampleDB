from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
import json

Base = declarative_base()

class Category(Base):
      __tablename__ = 'category'

      category_id = Column(Integer, primary_key=True)
      name = Column(String)
      last_update = Column(DateTime(timezone=False))

