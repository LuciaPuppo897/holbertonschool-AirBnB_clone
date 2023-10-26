#!/usr/bin/python3
"""Creates a basic command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '

    dicm = ['BaseModel', 'FileStorage', 'Amenity'
            'Place', 'Review', 'State', 'User']

    def do_EOF(self, arg):
        """Exit the interpreter"""
        return True

    def do_quit(self, arg):
        """Exit the interpreter"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, *args):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id."""
        arg = args.split()
        if arg not in dic:
            print("** class name missing **")
        if arg[0] not in FileStorage:
            print("** class doesn't exist **")
        obj.save()
        json.dump(dict_s, file)
        print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id."""
        arg = args.split()
        if arg not in dicm:
            print("** class name missing **")
        if arg[0] not in HBNBCommand:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        if arg[0] not in dicm and arg[1] == id:
            print("** no instance found **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)."""
        arg = args.split()
        if arg not in dic:
            print("** class name missing **")
        if arg[0] not in FileStorage:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        if arg[0] not in dic and arg[1] == id:
            print("** no instance found **")
        del (obj)

    def do_all(self, *args):
        """Prints all string representation of all instances
        based or not on the class name."""
        arg = args.split()
        if arg not in dic:
            print("** class name missing **")
        if arg[0] not in FileStorage:
            print("** class doesn't exist **")
        if args == dicm:
            print(obj)

    def do_update(self, *args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        arg = args.split()
        if arg not in dic:
            print("** class name missing **")
        if arg[0] not in HBNBCommand:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        if arg[0] not in dic and arg[1] == id:
            print("** no instance found **")
        if arg[2] not in HBNBCommand:
            print("** attribute name missing **")
        if arg[3] not in HBNBCommand:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
