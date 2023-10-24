#!/usr/bin/python3
"""
a class FileStorage that storage all of commands,date,classes etc
"""

import json
from os.path import isfile

class FileStorage:
    """def FileStorage class to storage a"""
    
    __file_path = "file.json"
    __objects = {}

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
        if isfile (FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
        else:
            pass
