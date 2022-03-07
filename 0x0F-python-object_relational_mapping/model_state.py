#!/usr/bin/python3
"""
Define a class State that inherits from Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    A class State that inherits from Base
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
