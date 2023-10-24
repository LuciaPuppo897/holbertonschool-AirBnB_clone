#!/usr/bin/python3
""" Base class:
id: string - assign with an uuid when an instance is created.
created_at: datetime - assign with the current datetime when an instance is
created.
updated_at: datetime - assign with the current datetime when an instance
is created  and it will be updated every time you change your object.
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string of the class, id, and dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the attribute updated_at to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys of __dict__"""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        return dict_
