"""Command Line Interface for the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from librarian.library import Library
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
        self.prompt = "[HOME]>"
        dbname = "library.lbr" if dbname is None else dbname
        self.library = Library(dbname)
        if not os.path.exists(dbname):
            self.library.create_db()

    def do_edit(self, args):
        """Edit a card. Can take a card code to edit."""
        code = int(args[0]) if args else 0

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

        cle = CLE(code=code, loadstring=loadstring)
        cle.cmdloop()
        card = cle.card

        if card is None:
            return clear()

        if card.code in codes:
            with self.library.connection() as libdb:
                libdb.execute("DELETE from CARDS where code = {0}".format(
                    card.code))
        self.library.save_card(card)
        clear()

    def do_delete(self, args):
        """Delete a card by code."""
        if args:
            code = int(args[0])
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

    def do_list(self, args):
        """List all stored cards. Can search by a code prefix."""
        codes = []
        with self.library.connection() as libdb:
            if args:
                codes = libdb.execute(
                    "SELECT code FROM CARDS WHERE code like ?",
                    (args[0] + '%',)).fetchall()
            else:
                codes = libdb.execute("SELECT code FROM CARDS").fetchall()

        if not len(codes):
            print("No cards could be found")

        for code in codes:
            card = self.library.load_card(code, False)
            print("{0}: {1}".format(card.code, card.name))
