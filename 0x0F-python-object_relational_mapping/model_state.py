#!/usr/bin/python3
""" This module marks the begining of using the ORM (sqlalchemy)
    to intereact with some databases as we prefer them. We will
    first begin with creating a Class"""

from SQLAlchemy import Column, Table, Integer, String
from SQLAlchemy.ext.declarative import declarative_base()

Base = declarative_base()


class State(Base):
    """ This is the class definition of the schema representation of
    the table of interest"""
    __tablename__ = "states"
    id = Column(
        Integer, primary_key=True, autoincrement=True,
        unique=True, nullable=False
        )
    name = Column(String(128), nullable=False)
