"""Command Line Interface for the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from librarian.library import Library


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


class CLI(object):
    """The command line inteface."""
    def __init__(self, dbname="library.lbr"):
        """
        Takes a filename for the database and will create it and any required
        tables if the database filename doesnt exist.
        """
        self.library = Library(dbname)
        if not os.path.exists(dbname):
            self.library.create_db()
        self.running = True
        self.commands = {"quit": self.quit,
                         "edit": self.edit,
                         "list": self.list,
                         "help": self.help}

    def quit(self, *_):
        """Save all changes and exit."""
        self.running = False

    def edit(self, *args):
        """
        Edit a card. Will ask for a code and create a card if the code is
        unused.
        """
        pass

    def list(self, *args):
        """
        List all registered card codes and their names. A code prefix may be
        entered to limit the selection.
        """
        codes = []
        with self.library.connection() as libdb:
            if args:
                codes = libdb.execute(
                    "SELECT code FROM CARDS WHERE code like ?",
                    ("{0}%".format((args[0]))))
            else:
                codes = libdb.execute("SELECT code FROM CARDS")

        for code in codes:
            card = self.library.load_card(code, False)
            print("{0}: {1}".format((card.code, card.name)))

    def help(self, *_):
        """Display information on possible top level commands."""
        for key, value in self.commands.items():
            print("{0}: {1}".format((key, value.__doc__)))

    def top_level(self):
        """
        The top level of the command line interface. Simply interprets
        commands until quit.
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
