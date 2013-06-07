"""Command Line Interface for the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from collections import OrderedDict
from librarian.library import Library
from .cle import CLE


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
    def __init__(self, dbname=None):
        """
        Takes a filename for the database and will create it and any required
        tables if the database filename doesnt exist.
        """
        dbname = "library.lbr" if dbname is None else dbname
        self.library = Library(dbname)
        if not os.path.exists(dbname):
            self.library.create_db()
        self.running = True
        self.commands = OrderedDict([
            ("quit", self.quit),
            ("edit", self.edit),
            ("delete", self.delete),
            ("list", self.list),
            ("help", self.help)
        ])

    def quit(self, *_):
        """Save all changes and gracefully exit."""
        self.running = False

    def edit(self, *args):
        """Edit a card. Can take a card code to edit."""
        code = int(args[0][0]) if len(args) and args[0] else 0

        with self.library.connection() as libdb:
            codes = libdb.execute("SELECT code FROM CARDS").fetchall()
        codes = [fetched[0] for fetched in codes]

        loadstring = None
        if code in codes:
            with self.library.connection() as libdb:
                loadstring = libdb.execute(
                    "SELECT card FROM CARDS WHERE code = {0}".format(
                        str(code))).fetchone()
                loadstring = loadstring[0] if loadstring else None

        card = CLE(loadstring=loadstring).top_level()

        if card is None:
            return None

        if card.code in codes:
            with self.library.connection() as libdb:
                libdb.execute("DELETE from CARDS where code = {0}".format(
                    card.code))
        self.library.save_card(card)
        self.header()

    def delete(self, *args):
        """Delete a card by code."""
        if args and args[0]:
            code = int(args[0][0])
        else:
            clear()
            print("Input code to delete.")
            code = int(readinput("|>"))

        with self.library.connection() as libdb:
            codes = libdb.execute("SELECT code FROM CARDS").fetchall()
        codes = [fetched[0] for fetched in codes]

        if code in codes:
            with self.library.connection() as libdb:
                libdb.execute("DELETE from CARDS where code = {0}".format(
                    code))
        else:
            print("No card could be found to delete")

    def list(self, *args):
        """List all stored cards. Can search by a code prefix."""
        codes = []
        with self.library.connection() as libdb:
            if args and args[0]:
                codes = libdb.execute(
                    "SELECT code FROM CARDS WHERE code like ?",
                    (args[0][0] + '%',)).fetchall()
            else:
                codes = libdb.execute("SELECT code FROM CARDS").fetchall()

        if not len(codes):
            print("No cards could be found")

        for code in codes:
            card = self.library.load_card(code, False)
            print("{0}: {1}".format(card.code, card.name))

    def help(self, *_):
        """Display information on possible top level commands."""
        for key, value in self.commands.items():
            print("{0}: {1}".format(key, value.__doc__))

    def header(self):
        """Display a header of information."""
        print(" " * 8, *self.commands.keys())

    def top_level(self):
        """
        The top level of the command line interface. Simply interprets
        commands until quit.
        """
        clear()
        self.header()
        while self.running:
            string = readinput("|>")
            parts = string.split(" ")
            command = parts[0]
            args = [] if len(parts) <= 1 else parts[1:]

            clear()
            self.header()
            if command not in self.commands:
                self.help()
                continue
            else:
                self.commands[command](args)
        clear()
