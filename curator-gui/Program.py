from __future__ import print_function
__version__ = "0.1.0"
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application
import MainForm
import argparse
import sys
import os

parser = argparse.ArgumentParser(description =
								"library access from the command line.")
parser.add_argument("-v", "--version", help="Display curator-gui version",
					action="store_true", default = False)
parser.add_argument("--libname", help="Path to the librarian library file",
					type=str, default = None)
args = parser.parse_args()

if args.version:
	print('curator-gui v' + __version__)
	sys.exit(0)

Application.EnableVisualStyles()
form = MainForm.MainForm(args.libname)
Application.Run(form)
