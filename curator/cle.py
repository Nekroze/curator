"""Command Line Editor for cards with the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from librarian.card import Card
from .cli import readinput, clear


class CLE(object):
    """The command line editor for cards."""
    def __init__(self, *args):
        """
        Can take up to two arguments to define the code and name of the new
        card before starting the edit although it is optional.
        """
        self.library = library
        self.running = True
        self.commands = {"commit": self.commit,
                         "cancel": self.cancel,
                         "help": self.help
                         }
        if len(args) > 1:
            self.card = Card(int(args[0]), args[1])
        elif len(args) == 1:
            self.card = Card(int(args[0]))
        else:
            self.card = Card()

    def commit(self, *_):
        """Save all changes and exit."""
        self.running = False

    def commit(self, *_):
        """Exit without saving changes."""
        self.card = None
        self.running = False

    def help(self, *_):
        """Display information on possible card editing commands."""
        for key, value in self.commands.items():
            print("{0}: {1}".format((key, value.__doc__)))

    def top_level(self):
        """
        The top level of the command line editor for cards. Simply interprets
        commands until quit at which time it returns the edited card.
        """
        while self.running:
            string = readinput("|>")
            parts = string.split(string, " ")
            command = parts[0]
            args = [] if len(parts) > 1 else parts[1:]

            clear()
            if command not in self.commands:
                self.help()
                continue
            else:
                self.commands[command](args)
        return self.card
