# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Employee(Base):
    __tablename__ = 'employee'

    Employee_id = Column(Integer, primary_key=True)
    First_name = Column(String(50))
    Last_name = Column(String(50))
    Salary = Column(Integer)
    Joining_date = Column(Date)
    department = Column(String(50))


t_reward = Table(
    'reward', metadata,
    Column('Employee_ref_id', ForeignKey('employee.Employee_id'), index=True),
    Column('date_reward', Date),
    Column('amount', Integer)
)
