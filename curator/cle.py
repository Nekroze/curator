"""Command Line Editor for cards with the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from collections import OrderedDict
from librarian.card import Card


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


class CLE(object):
    """The command line editor for cards."""
    def __init__(self, code=None, loadstring=None):
        """
        Can take up to two arguments to define the code and name of the new
        card before starting the edit although it is optional.
        """
        self.running = True
        self.commands = OrderedDict([
            ("code", self.code),
            ("name", self.name),
            ("attribute", self.attribute),
            ("ability", self.ability),
            ("info", self.info),
            ("delete", self.delete),
            ("commit", self.commit),
            ("cancel", self.cancel),
            ("help", self.help)
        ])
        self.card = Card(code=code, loadstring=loadstring)

    def commit(self, *_):
        """Save all changes and exit."""
        self.running = False

    def cancel(self, *_):
        """Exit without saving changes."""
        self.card = None
        self.running = False

    def help(self, *_):
        """Display information on possible card editing commands."""
        for key, value in self.commands.items():
            print("{0}: {1}".format(key, value.__doc__))

    def code(self, *args):
        """Input a new code for the current card."""
        if args:
            self.card.code = int(args[0])
        else:
            clear()
            print("Input new code.")
            self.card.code = int(readinput("|>"))

    def name(self, *args):
        """Input a new name for the current card."""
        if args:
            self.card.name = " ".join(args)
        else:
            clear()
            print("Input new name.")
            self.card.name = readinput("|>")

    def attribute(self, *args):
        """Add a new attribute."""
        if args:
            self.card.add_attribute(" ".join(args))
        else:
            clear()
            print("Input attribute.")
            self.card.add_attribute(readinput("|>"))

    def ability(self, *args):
        """Add a new ability."""
        if len(args) > 1:
            self.card.add_ability(args[0], " ".join(args[1:]))
        else:
            clear()
            print("Input phase for ability.")
            phase = readinput("|>")
            print("Input ability.")
            ability = readinput("|>")
            self.card.add_ability(phase, ability)

    def info(self, *args):
        """Add a new info field."""
        if len(args) > 1:
            self.card.set_info(args[0], " ".join(args[1:]), True)
        else:
            clear()
            print("Input info key.")
            key = readinput("|>")
            print("Input info value.")
            value = readinput("|>")
            self.card.set_info(key, value, True)

    def delete(self, *_):
        """Delete an index from a given field."""
        self.header()
        print("Field")
        field = readinput("|>")

        if field == "attribute":
            print("Index")
            index = readinput("|>")
            del self.card.attribute[int(index)]
        elif field == "ability":
            print("Key")
            key = readinput("|>")
            print("Index")
            index = readinput("|>")
            if index:
                del self.card.ability[key][int(index)]
            else:
                del self.card.ability[key]
        elif field == "info":
            print("Key")
            key = readinput("|>")
            print("Index")
            index = readinput("|>")
            if index:
                del self.card.info[key][int(index)]
            else:
                del self.card.info[key]
        else:
            print("Field not accepted. Must be; attribute, ability or info.")

    def header(self):
        """
        Display a header of information.
        """
        clear()
        print(" " * 8, *self.commands.keys())
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
                print("    >[{1}] {0}".format(ability, index))

        print(":::::Info")
        for key, value in self.card.info.items():
            print("{0}".format(key))
            for index, info in enumerate(value):
                print("    >[{1}] {0}".format(info, index))
        print("=============================================")

    def top_level(self):
        """
        The command line editor for cards. Simply interprets
        commands until quit at which time it returns the edited card.
        """
        self.header()
        while self.running:
            string = readinput("|>")
            parts = string.split(" ")
            command = parts[0]
            args = [] if len(parts) <= 1 else parts[1:]

            self.header()
            if command not in self.commands:
                self.help()
                continue
            else:
                self.commands[command](*args)
                self.header()
        clear()
        return self.card
