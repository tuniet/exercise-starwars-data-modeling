import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    desc = Column(String(120), nullable = False)
    hair_color = Column(String(120), nullable=False)
    eye_color = Column(String(120), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    desc = Column(String(120), nullable = False)
    climate = Column(String(120), nullable=False)
    population = Column(Integer, nullable=False)

class FavouritePlanets(Base):
    __tablename__ = 'favouritePlanets'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey("user.id"))
    planetid = Column(Integer, ForeignKey("planet.id"))
    user = relationship(User)
    planet = relationship(Planet)

class FavouriteCharacters(Base):
    __tablename__ = 'favouriteCharacters'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey("user.id"))
    characterid = Column(Integer, ForeignKey("character.id"))
    user = relationship(User)
    character = relationship(Character)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
