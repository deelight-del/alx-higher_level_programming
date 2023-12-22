#!/usr/bin/python3
"""The class definition of a model_city
for City class for ORM mapping"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """City class definition for ORM mapping"""
    __tablename__ = 'cities'
    id = Column(
        Integer, autoincrement=True, nullable=False,
        primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
