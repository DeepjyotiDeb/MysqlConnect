from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table
from database import engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# class BlogDetails(Base):
#     __tablename__ = 'blog-details'
#     id = Column(Integer, primary_key= True, index = True)
#     title = Column(String(20))
#     summary = Column(String)

class Employee1(Base):
    employee = Base.classes.Employee



    # __table__ = Table('employee',                    
    #                  Base.metadata, Column("id",Integer, primary_key=True),
    #                 autoload=True, autoload_with=engine)
    # __tablename__ = 'employee'
    # id = Column(Integer, primary_key=True)
    # bars = relationship("Reward")

# class Reward(Base):
#     __tablename__ = 'reward'
#     Employee_ref_id = Column(Integer, ForeignKey('Employee.id'))