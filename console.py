#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    valid_keys = {
        "BaseModel": ["id", "created_at", "updated_at"],
        "User": [
            "id",
            "created_at",
            "updated_at",
            "email",
            "password",
            "first_name",
            "last_name",
        ],
        "City": ["id", "created_at", "updated_at", "state_id", "name"],
        "State": ["id", "created_at", "updated_at", "name"],
        "Place": [
            "id",
            "created_at",
            "updated_at",
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ],
        "Amenity": ["id", "created_at", "updated_at", "name"],
        "Review": ["id", "created_at", "updated_at",
                   "place_id", "user_id", "text"],
    }

    dot_cmds = ["all", "count", "show", "destroy", "update"]
    types = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    def precmd(self, arguments):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ""

        if not ("." in arguments and "(" in arguments and ")" in arguments):
            return arguments

        try:
            parse_line = arguments[:]

            _cls = parse_line[: parse_line.find(".")]

            _cmd = parse_line[parse_line.find(".") + 1: parse_line.find("(")]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            parse_line = parse_line[parse_line.find("(") + 1: parse_line.find(")")]
            if parse_line:
                parse_line = parse_line.partition(", ")

                _id = parse_line[0].replace('"', "")

                parse_line = parse_line[2].strip()
                if parse_line:
                    if (
                        parse_line[0] == "{"
                        and parse_line[-1] == "}"
                        and type(eval(parse_line)) is dict
                    ):
                        _args = parse_line
                    else:
                        _args = parse_line.replace(",", "")
            arguments = " ".join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return arguments

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print("(hbnb) ", end="")
        return stop

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def parse_value(self, value):
        """cast string to float or int if possible"""
        valid = True
        if len(value) >= 2 and value[0] == '"'\
                and value[len(value) - 1] == '"':
            value = value[1:-1]
            value = value.replace("_", " ")
        else:
            try:
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                valid = False

        if valid:
            return value
        else:
            return None

    def do_create(self, args):
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        arguments = args.split()
        class_name = arguments[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        for param_index in range(1, len(arguments)):
            param_array = arguments[param_index].split("=")
            if len(param_array) == 2:
                key = param_array[0]
                if key not in HBNBCommand.valid_keys[class_name]:
                    continue
                value = self.parse_value(param_array[1])
                if value is not None:
                    setattr(new_instance, key, value)
            else:
                pass
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create method"""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method to show an individual object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help information for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(" ")[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split(".")[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)

    def help_all(self):
        """Help information for the all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage.all().items():
            if args == k.split(".")[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """Updates a certain object with new info"""
        c_name = c_id = attribute_name = attribute_value = kwargs = ""

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else: 
            print("** instance id missing **")
            return


        key = c_name + "." + c_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if "{" in args[2] and "}" in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  
            args = args[2]
            if args and args[0] == '"':
                second_quote = args.find('"', 1)
                attribute_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(" ")

            if not attribute_name and args[0] != " ":
                attribute_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '"':
                attribute_value = args[2][1: args[2].find('"', 1)]

            if not attribute_value and args[2]:
                attribute_value = args[2].partition(" ")[0]

            args = [attribute_name, attribute_value]

        new_dict = storage.all()[key]

        for i, attribute_name in enumerate(args):
            if i % 2 == 0:
                attribute_value = args[i + 1]
                if not attribute_name:
                    print("** attribute name missing **")
                    return
                if not attribute_value:
                    print("** value missing **")
                    return
                if attribute_name in HBNBCommand.types:
                    attribute_value = HBNBCommand.types[attribute_name](attribute_value)

                new_dict.__dict__.update({attribute_name: attribute_value})

        new_dict.save()

    def help_update(self):
        """Help information for the update class"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()