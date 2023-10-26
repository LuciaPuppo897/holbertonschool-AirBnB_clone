#!/usr/bin/python3
"""
a class FileStorage that storage all of commands,date,classes etc
"""

import json
from os.path import isfile
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.review import Review


class FileStorage:
    """def FileStorage class to storage a"""

    __file_path = "file.json"
    __objects = {}

    def path (self):
        """returns the file path of the given file"""
        return self.__file_path
    
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_s = {}
        for key, value in self.__objects.items():
            dict_s[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_s, file, default=lambda o: o.__dict__)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                class_name = value["__class__"]
                if class_name in globals():
                    class_obj = globals()[class_name](**value)
                    FileStorage.__objects[key] = class_obj
        else:
            pass
