"""Command Line Interface for the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from colorama import Fore
from librarian.library import Library
from librarian.card import Card
from .console import Console
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


class CLI(Console):
    """The command line inteface."""
    def __init__(self, dbname=None):
        """
        Takes a filename for the database and will create it and any required
        tables if the database filename doesnt exist.
        """
        Console.__init__(self)
        self.colormap = {}
        self.colormap["Cval"] = Fore.YELLOW
        self.colormap["Csym"] = Fore.GREEN
        self.colormap["Ckey"] = Fore.CYAN
        self.prompt = "{Csym}[{Ckey}HOME{Csym}]>".format(**self.colormap)
        dbname = "library.lbr" if dbname is None else dbname
        self.library = Library(dbname)
        if not os.path.exists(dbname):
            self.library.create_db()

    def do_edit(self, args):
        """Edit a card. Can take a card code to edit."""
        code = int(args) if args else 0
        card = self.library.load_card(code, cache=False)
        if card is None:
            card = Card(code)

        cle = CLE(self.colormap, card)
        cle.cmdloop()
        card = cle.card

        if card is None:
            return clear()

        self.library.save_card(card)
        clear()

    def do_delete(self, args):
        """Delete a card by code."""
        if args:
            code = int(args)
        else:
            clear()
            print("Input code to delete.")
            code = int(readinput("|>"))

        with self.library.connection() as libdb:
            libdb.execute("DELETE from CARDS where code = {0}".format(code))

    def do_list(self, args):
        """List all stored cards. Can search by a code prefix."""
        code = args if args else None
        results = self.library.filter_search(code=code)

        if not len(results):
            print("No cards could be found")
            return None

        for codename in results:
            print("{Cval}{0}{Csym}: {Cval}{1}".format(*codename,
                                                      **self.colormap))
