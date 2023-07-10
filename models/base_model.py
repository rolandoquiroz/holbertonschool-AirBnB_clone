#!/usr/bin/python3

"""
This module defines a BaseModel Class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A BaseModel class
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    