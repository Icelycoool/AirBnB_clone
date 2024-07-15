#!/bin/usr/bin/python3
"""
Module FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Custom class for File Storage.
    """

    __file_path = "file.json"
    __objects = {}
    imported_classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'City': City,
                'State': State,
                'Place': Place,
                'Review': Review
    }

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
                    if class_name in self.imported_classes:
                        obj_instance = self.imported_classes[class_name](**val)
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
