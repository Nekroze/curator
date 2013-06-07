"""Command Line Editor for cards with the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
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
        self.commands = {"commit": self.commit,
                         "cancel": self.cancel,
                         "help": self.help,
                         "code": self.code,
                         "name": self.name
                         }
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
        if args and args[0]:
            self.card.code = int(args[0][0])
        else:
            clear()
            print("Input new code.")
            self.card.code = int(readinput("|>"))

    def name(self, *args):
        """Input a new name for the current card."""
        if args and args[0]:
            self.card.name = args[0][0]
        else:
            clear()
            print("Input new name.")
            self.card.name = readinput("|>")

    def header(self):
        """
        Display a header of information.
        """
        print(*self.commands.keys())
        print("{0}: {1}".format(self.card.code, self.card.name))

    def top_level(self):
        """
        The command line editor for cards. Simply interprets
        commands until quit at which time it returns the edited card.
        """
        while self.running:
            self.header()
            string = readinput("|>")
            parts = string.split(" ")
            command = parts[0]
            args = [] if len(parts) <= 1 else parts[1:]

            clear()
            if command not in self.commands:
                self.help()
                continue
            else:
                self.commands[command](args)
        return self.card
