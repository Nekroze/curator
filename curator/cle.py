"""Command Line Editor for cards with the Librarian API."""
from __future__ import print_function
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import os
import sys
from colorama import Fore
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
        self.prompt = "{0}[{1}EDIT{0}]>{2}".format(Fore.GREEN,
                                                   Fore.RED, Fore.RESET)

    def do_commit(self, _):
        """
        Save all changes and exit.
        """
        return -1

    def do_exit(self, _):
        """
        Exit without saving changes.
        """
        self.card = None
        return -1

    def do_code(self, args):
        """
        ``code <newcode>`` Set the card code to <newcode>.
        """
        if args:
            args = [arg.strip() for arg in args.split()]
            self.card.code = int(args[0])
        self.header()

    def do_name(self, args):
        """
        ``name <newname>`` Set the card name to <newname>.
        """
        if args:
            args = [arg.strip() for arg in args.split()]
            self.card.name = " ".join(args)
        self.header()

    def do_attribute(self, args):
        """
        ``attribute <attr>`` Add <attr> to this cards attributes.
        """
        if args:
            args = [arg.strip() for arg in args.split()]
            self.card.add_attribute(" ".join(args))
        self.header()

    def do_ability(self, args):
        """
        ``ability <phase> <abi>`` Add <abi> to this cards abilities under
        <phase>.
        """
        if args:
            args = [arg.strip() for arg in args.split()]
            if len(args) > 1:
                self.card.add_ability(args[0], " ".join(args[1:]))
        self.header()

    def do_info(self, args):
        """
        ``info <key> <data>`` Add <data> to this cards info under <key>.
        """
        if args:
            args = [arg.strip() for arg in args.split()]
            if len(args) > 1:
                self.card.set_info(args[0], " ".join(args[1:]), True)
        self.header()

    def do_delete(self, args):
        """
        ``delete <field> <key/index> <index>`` delete info from the card
        under field and if required key and/then the index. Use the display
        header to get index's.
        """
        if args:
            args = [arg.strip() for arg in args.split()]
            field = args[0]
            if field == "attribute" and len(args) >= 2:
                if len(self.card.attributes) <= int(args[1]):
                    del self.card.attributes[int(args[1])]
                return self.header()
            elif field == "attribute":
                self.card.attributes = []
                return self.header()
            elif field == "ability" and len(args) >= 3:
                if args[1] in self.card.abilities and \
                        len(self.card.attributes[args[1]]) >= int(args[2]):
                    del self.card.abilities[args[1]][int(args[2])]
                return self.header()
            elif field == "ability" and len(args) >= 2:
                if args[1] in self.card.abilities:
                    del self.card.abilities[args[1]]
                return self.header()
            elif field == "ability":
                self.card.abilities = {}
                return self.header()
            elif field == "info" and len(args) >= 3:
                if args[1] in self.card.info and \
                        len(self.card.info[args[1]]) >= int(args[2]):
                    del self.card.info[args[1]][int(args[2])]
                return self.header()
            elif field == "info" and len(args) >= 2:
                if args[1] in self.card.info:
                    del self.card.info[args[1]]
                return self.header()
            elif field == "info":
                self.card.info = {}
                return self.header()
        self.header()

    def header(self):
        """Display a header of card information."""
        clear()
        if self.card is None:
            return None
        print("{2}{0}{3}: {2}{1}{3}".format(self.card.code, self.card.name,
                                            Fore.BLUE, Fore.RED, Fore.RESET))

        print("{0}:::::{1}Attributes{2}".format(Fore.GREEN, Fore.RED,
                                                Fore.RESET))
        for index, attribute in enumerate(self.card.attributes):
            print("{3}[{2}{0}{3}]{2}{1}{3}".format(str(index), attribute,
                                                   Fore.BLUE, Fore.RED,
                                                   Fore.RESET))

        print("{0}:::::{1}Abilities{2}".format(Fore.GREEN, Fore.RED,
                                               Fore.RESET))
        for phase, abilities in self.card.abilities.items():
            print("{1}{0}{2}".format(phase, Fore.BLUE, Fore.RESET))
            for index, ability in enumerate(abilities):
                print("|_____{3}[{2}{0}{3}]{2}{1}{3}".format(str(index),
                                                             ability,
                                                             Fore.BLUE,
                                                             Fore.RED,
                                                             Fore.RESET))

        print("{0}:::::{1}Info{2}".format(Fore.GREEN, Fore.RED,
                                          Fore.RESET))
        for key, value in self.card.info.items():
            print("{1}{0}{2}".format(key, Fore.BLUE, Fore.RESET))
            for index, info in enumerate(value):
                print("|_____{3}[{2}{0}{3}]{2}{1}{3}".format(str(index), info,
                                                             Fore.BLUE,
                                                             Fore.RED,
                                                             Fore.RESET))

    def preloop(self):
        """Display header at start."""
        super(CLE, self).preloop()
        self.header()
