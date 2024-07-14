#!/usr/bin/python3
"""
Entry point to the commant interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AIRBNB_CLONE"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        point()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_help(self, arg):
        """List available commands with 'help' or
        detailed help with 'help <command>'"""
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
