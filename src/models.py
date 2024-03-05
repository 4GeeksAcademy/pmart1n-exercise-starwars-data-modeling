import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable= False, unique=True)
    password = Column(String(16), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(50))

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    body = Column(String(2000), nullable=False)
    img_url = Column(String)
    user_id = Column(Integer, ForeignKey('users_id'))
    users = relationship(Users)

    def to_dict(self):
        return {}


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(String(50), primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets_id'))
    homeworld = relationship('Planets')


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    director = Column(String(50), nullable=False)
    year = Column(DateTime)


class Character_Films(Base):
    __tablename__ = 'character_films'
    id = Column(Integer, primary_key=True)
    minutes = Column(DateTime)
    Character_id = Column, ForeignKey('characters.id')
    film_id = Column(Integer, ForeignKey('films.id'))
    character = relationship('character', foreign_keys=['character_id'])
    film = relationship('film', foreign_keys=['film_id'])


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
