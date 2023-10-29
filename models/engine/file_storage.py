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
        with open(self.__class__.__file_path, 'w', encoding='utf-8') as file:
            for key in self.__class__.__objects.items():
                dict_s[key] = self.__class__.__objects[key].to_dict()
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
                for key, value in loaded_data.items():
                    if '__class__' in value:
                        class_name = value['__class__']
                    if class_name in dict_classs:
                        cls = dict_classs[class_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
