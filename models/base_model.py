#!/usr/bin/python3
"""
Defined the base model for the AirBNB_clone
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A base class for other models.

    Attributes:
            id (str): Unique identifier for each instance of BaseModel.
            created_at (datetime): The datetime when the intance is created.
            updated_at (datetime): The datetime when the instance is modified.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialized a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing all keys/values
                 of __dict__ of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
