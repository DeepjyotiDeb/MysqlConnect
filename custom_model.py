# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BlogDetail(Base):
    __tablename__ = 'blog-details'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20))
    summary = Column(String(20))
