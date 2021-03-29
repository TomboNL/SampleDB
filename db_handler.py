from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from category import Category
import json
from sqlalchemy.ext.declarative import DeclarativeMeta



class DB_handler():

    global engine
    global session

    def __init__(self):
        engine = create_engine("postgresql+psycopg2://postgres:djaivi2015@localhost/dvdrental")
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getCategoryList(self):
        return self.session.query(Category).all()

    def getCategory(self, id):
        return self.session.query(Category).filter_by(category_id=id).all()

    def addCategory(self, category):
        self.session.add(category)
        self.session.commit()




