#!/usr/bin/python3

import webbrowser
import sys
import re
import pyperclip

if len(sys.argv) > 1:
    address_string = re.sub(" ", "+", " ".join(sys.argv[1:]))
else:
    address_string = pyperclip.paste()
# address_string = " ".join(sys.argv[1:]) you could use this also

webbrowser.open("https://www.google.com/maps/place/" + address_string)
