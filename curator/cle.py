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
    def __init__(self, loadstring=None):
        """
        Can take up to two arguments to define the code and name of the new
        card before starting the edit although it is optional.
        """
        self.running = True
        self.commands = OrderedDict([
            ("code", self.code),
            ("name", self.name),
            ("commit", self.commit),
            ("cancel", self.cancel),
            ("help", self.help)
        ])
        self.card = Card(loadstring=loadstring)

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
        self.header()

    def name(self, *args):
        """Input a new name for the current card."""
        if len(args) > 1:
            self.card.name = " ".join(args)
        elif args:
            self.card.name = args[0]
        else:
            clear()
            print("Input new name.")
            self.card.name = readinput("|>")
        self.header()

    def attribute(self, *args):
        """Add a new attribute."""
        if len(args) > 1:
            self.card.add_attribute(" ".join(args))
        elif args:
            self.card.add_attribute(args[0])
        else:
            clear()
            print("Input attribute.")
            self.card.add_attribute(readinput("|>"))
        self.header()

    def header(self):
        """
        Display a header of information.
        """
        clear()
        print(" " * 8, *self.commands.keys())
        print("{0}: {1}".format(self.card.code, self.card.name))
        print(":::::Attributes")
        for attribute in self.card.attributes:
            print(attribute)
        print(":::::Abilities")
        for phase, abilities in self.card.abilities.items():
            print("<{0}>".format(phase))
            for ability in abilities:
                print("    >{0}".format(ability))
        print(":::::Info")
        for key, value in self.card.info.items():
            print("{0}: {1}".format(key, value))

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
        clear()
        return self.card
