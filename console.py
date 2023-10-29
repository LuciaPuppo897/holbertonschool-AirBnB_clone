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
from models.amenity import Amenity


valid_classes = {'BaseModel', 'FileStorage', 'City',
                 'Place', 'Review', 'State', 'User', 'Amenity'}


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = '(hbnb) '
    help = 'Documented commands (type help <topic>):'

    def do_EOF(self, arg):
        """Exit the interpreter"""
        return True

    def do_quit(self, arg):
        """Exit the interpreter"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it to the JSON file,
        and prints the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            instance = storage.all()[key]  # take the value in the dic
            print(instance)   # made with storage.save
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save it in the JSON file)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()  # save the change made by delete
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of instances
        of the given class name, or all instances if no
        name is given
        """
        args = arg.split()
        instances = storage.all()
        if len(args) == 0:
            instance_list = []
            for k, v in instances.items():
                instance_list.append(str(v))
            print(instance_list)
        else:
            cls_n = args[0]
            if cls_n not in valid_classes:
                print("** class doesn't exist **")
                return
            if cls_n:
                class_instances = [v for k, v in instances.items() if cls_n in k]
                print([str(instances) for instances in class_instances])
            else:
                print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating an attribute
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()  # call the save method


if __name__ == '__main__':
    HBNBCommand().cmdloop()
