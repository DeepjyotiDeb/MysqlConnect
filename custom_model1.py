# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    release_year = Column(Integer)
    band_id = Column(ForeignKey('bands.id'), nullable=False, index=True)

    band = relationship('Band')


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    length = Column(Float, nullable=False)
    album_id = Column(ForeignKey('albums.id'), nullable=False, index=True)

    album = relationship('Album')
