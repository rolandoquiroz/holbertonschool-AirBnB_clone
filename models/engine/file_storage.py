#!/usr/bin/python3

"""
This module defines a FileStorage Class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    A FileStorage class
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            objects = {key: value.to_dict()
                       for key, value in self.__objects.items()}
            f.write(json.dumps(objects))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_object = json.loads(f.read())
                objects = {key: BaseModel(value)
                           for key, value in json_object.items()}
                self.__objects = objects
