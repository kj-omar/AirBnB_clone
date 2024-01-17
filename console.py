#!/usr/bin/python3
"""Defining the modules used in the project"""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the the command environment and methods used in the process"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty spaces."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            list_of_args = line.split(" ")

            kwargs = {}
            for i in range(1, len(list_of_args)):
                key, value = tuple(list_of_args[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                object = eval(list_of_args[0])()
            else:
                object = eval(list_of_args[0])(**kwargs)
                storage.new(object)
            print(object.id)
            object.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        try:
            if not line:
                raise SyntaxError()
            list_of_args = line.split(" ")
            if list_of_args[0] not in self.__classes:
                raise NameError()
            if len(list_of_args) < 2:
                raise IndexError()
            objects = storage.all()
            key = list_of_args[0] + '.' + list_of_args[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if not line:
            o = storage.all()
            print([o[k].__str__() for k in o])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            o = storage.all(eval(args[0]))
            print([o[k].__str__() for k in o])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when the args is not consistent with their values
            NameError: when there are no object that have the name desiered
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            list_of_args = split(line, " ")
            if list_of_args[0] not in self.__classes:
                raise NameError()
            if len(list_of_args) < 2:
                raise IndexError()
            objects = storage.all()
            key = list_of_args[0] + '.' + list_of_args[1]
            if key not in objects:
                raise KeyError()
            if len(list_of_args) < 3:
                raise AttributeError()
            if len(list_of_args) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[list_of_args[2]] = eval(list_of_args[3])
            except Exception:
                v.__dict__[list_of_args[2]] = list_of_args[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """count the number of instances of a class
        """
        count_num = 0
        try:
            list_of_args = split(line, " ")
            if list_of_args[0] not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == list_of_args[0]:
                    count_num += 1
            print(count_num)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        list_of_args = []
        list_of_args.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            list_of_args.append(((new_str.split(", "))[0]).strip('"'))
            list_of_args.append(my_dict)
            return list_of_args
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        list_of_args.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in list_of_args)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        list_of_args = line.split('.')
        if len(list_of_args) >= 2:
            if list_of_args[1] == "all()":
                self.do_all(list_of_args[0])
            elif list_of_args[1] == "count()":
                self.count(list_of_args[0])
            elif list_of_args[1][:4] == "show":
                self.do_show(self.strip_clean(list_of_args))
            elif list_of_args[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(list_of_args))
            elif list_of_args[1][:6] == "update":
                args = self.strip_clean(list_of_args)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()