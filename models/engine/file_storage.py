#!/usr/bin/python3
"""
a class FileStorage that storage all of commands,date,classes etc
"""

import json


class FileStorage:
    """def FileStorage class to storage a"""

    __file_path = "file.json"
    __objects = {}

    def path(self):
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
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dict_s, file, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                from models.user import User
                from models.city import City
                from models.state import State
                from models.place import Place
                from models.amenity import Amenity
                from models.review import Review
                from models.base_model import BaseModel

                dict_classs = {
                    "User": User,
                    "City": City,
                    "State": State,
                    "Place": Place,
                    "Amenity": Amenity,
                    "Review": Review,
                    "BaseModel": BaseModel
                }
                for key, obj in loaded_data.items():
                    dict_classs[key] = dict_classs[obj["__class__"]](**obj)
        except FileNotFoundError:
            pass
