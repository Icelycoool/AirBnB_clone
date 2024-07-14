#!/usr/bin/python3
"""
Entry point to the commant interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for AIRBNB_CLONE
    """
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D)
        """
        point()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        save it and print the id
        """""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        obj_list = [str(obj) for key, obj in objects.items()
                    if not arg or key.startswith(arg + '.')]
        print(obj_list)

    def do_update(self, arg):
        """
        pdates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print("** invalid value **")
                return
        else:
            attr_value = str(attr_value)

        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_help(self, arg):
        """
        List available commands with 'help' or
        detailed help with 'help <command>'
        """
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
