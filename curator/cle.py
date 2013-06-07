"""Command Line Editor for cards with the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from librarian.card import Card
from .console import Console


def readinput(prefix):
    """Python version independent input reading."""
    if sys.version_info > (3, 0):
        return input(prefix)
    else:
        return raw_input(prefix)


def clear():
    """Platform independent clear console screen."""
    if "windows" not in sys.platform.lower():
        os.system("clear")
    else:
        os.system("cls")


class CLE(Console):
    """The command line editor for cards."""
    def __init__(self, code=None, loadstring=None):
        """
        Can take up to two arguments to define the code and name of the new
        card before starting the edit although it is optional.
        """
        Console.__init__(self)
        self.card = Card(code=code, loadstring=loadstring)
        self.prompt = "[EDIT]>"

    def do_commit(self, _):
        """Save all changes and exit."""
        return -1

    def do_exit(self, _):
        """Exit without saving changes."""
        self.card = None
        return -1

    def do_code(self, args):
        """Input a new code for the current card."""
        if args:
            args = [arg.strip() for arg in args.split()]
            self.card.code = int(args[0])
        else:
            print("Input new code.")
            self.card.code = int(readinput(self.prompt))
        self.header()

    def do_name(self, args):
        """Input a new name for the current card."""
        if args:
            args = [arg.strip() for arg in args.split()]
            self.card.name = " ".join(args)
        else:
            print("Input new name.")
            self.card.name = readinput(self.prompt)
        self.header()

    def do_attribute(self, args):
        """Add a new attribute."""
        if args:
            args = [arg.strip() for arg in args.split()]
            self.card.add_attribute(" ".join(args))
        else:
            print("Input attribute.")
            self.card.add_attribute(readinput(self.prompt))
        self.header()

    def do_ability(self, args):
        """Add a new ability."""
        if args:
            args = [arg.strip() for arg in args.split()]
            if len(args) > 1:
                self.card.add_ability(args[0], " ".join(args[1:]))
            else:
                self.do_ability(self, None)
        else:
            print("Input phase for ability.")
            phase = readinput(self.prompt)
            print("Input ability.")
            ability = readinput(self.prompt)
            self.card.add_ability(phase, ability)
        self.header()

    def do_info(self, args):
        """Add a new info field."""
        if args:
            args = [arg.strip() for arg in args.split()]
            if len(args) > 1:
                self.card.set_info(args[0], " ".join(args[1:]), True)
            else:
                self.do_info(self, None)
        else:
            print("Input info key.")
            key = readinput(self.prompt)
            print("Input info value.")
            value = readinput(self.prompt)
            self.card.set_info(key, value, True)
        self.header()

    def do_delete(self, args):
        """Delete an index from a given field."""
        if args:
            args = [arg.strip() for arg in args.split()]
            field = args[0]
            if field == "attribute" and len(args) >= 2:
                del self.card.attributes[int(args[1])]
                return self.header()
            elif field == "ability" and len(args) >= 3:
                del self.card.abilities[args[1]][int(args[2])]
                return self.header()
            elif field == "ability" and len(args) >= 2:
                del self.card.abilities[args[1]]
                return self.header()
            elif field == "info" and len(args) >= 3:
                del self.card.info[args[1]][int(args[2])]
                return self.header()
            elif field == "info" and len(args) >= 2:
                del self.card.info[args[1]]
                return self.header()

        print("Field")
        field = readinput(self.prompt)

        if field == "attribute":
            print("Index")
            index = readinput(self.prompt)
            del self.card.attributes[int(index)]
        elif field == "ability":
            print("Key")
            key = readinput(self.prompt)
            print("Index")
            index = readinput(self.prompt)
            if index:
                del self.card.abilities[key][int(index)]
            else:
                del self.card.abilities[key]
        elif field == "info":
            print("Key")
            key = readinput(self.prompt)
            print("Index")
            index = readinput(self.prompt)
            if index:
                del self.card.info[key][int(index)]
            else:
                del self.card.info[key]
        else:
            print("Field not accepted. Must be; attribute, ability or info.")
        self.header()

    def header(self, args=None):
        """Display a header of card information."""
        clear()
        if self.card is None:
            return None
        print("{0}: {1}".format(self.card.code, self.card.name))

        print(":::::Attributes")
        for index, attribute in enumerate(self.card.attributes):
            print("[{0}]".format(str(index)), attribute)

        print(":::::Abilities")
        for phase, abilities in self.card.abilities.items():
            print("{0}".format(phase))
            for index, ability in enumerate(abilities):
                print("    [{1}] {0}".format(ability, index))

        print(":::::Info")
        for key, value in self.card.info.items():
            print("{0}".format(key))
            for index, info in enumerate(value):
                print("    [{1}] {0}".format(info, index))

    def preloop(self):
        """Display header at start."""
        super(CLE, self).preloop()
        self.header()
