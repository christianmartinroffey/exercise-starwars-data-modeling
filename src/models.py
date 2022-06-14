import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    homeworld = Column(String (50), nullable=False)
    height = Column (Integer, nullable=False)
    mass = Column (Integer, nullable=False)
    hair_color = Column(String(50), nullable=True)
    skin_color = Column (String(50), nullable=False)
    eye_color = Column (String(50), nullable=False)
    birth_year = Column (String(50), nullable=False)
    gender = Column (String(10), nullable=False)

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String (50), nullable=False)
    terrain = Column (String(50), nullable=False)
    suface_water = Column (Integer, nullable=False)
    rotation_period = Column (Integer, nullable=False)
    diameter = Column (Integer, nullable=False)
    orbital_period = Column (Integer, nullable=False)
    gravity = Column (Integer, nullable=False)
    population = Column (Integer, nullable=False)

class User(Base):
    __tablename__ = 'User'
    id = Column (Integer, primary_key=True)
    email = Column (String, unique=True)
    password = Column (String (8), nullable=False)
    favourite_planet = Column (String, nullable=True)
    favourite_character = Column (String, nullable=True)

# relational table
class CharacterHomeworld(Base):
    __tablename__ = 'CharacterHomeworld'
    characterID = Column(Integer, ForeignKey('character.ID'), primary_key=True)
    homeworld = Column(Integer, ForeignKey('planet.name'))
    

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')