#!/bin/usr/bin/python3
"""
Module FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Custom class for File Storage.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns dictionary representation of all onjects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    class_name, obj_id = key.split('.')

                    if class_name == "BaseModel":
                        obj_instance = BaseModel(**val)
                    elif class_name == "User":
                        obj_instance = User(**val)

                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
