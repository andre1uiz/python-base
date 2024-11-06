#!/app/python-base/.venv/bin/python
""" Bloco de notas

$ notes.py new "Minha Nota"
tag: Tech
Text: 
Anotação geral sobre carreira de tecnologia
$
...
...
$ notes.py read tech
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    print("you must specify a subcommand", cmds)
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath, 'r'):
        title, tag, text = line.split("\t")
        try:
            if tag.lower() == arguments[1].lower():
                print(f"Title: {title}")
                print(f"text: {text}")
                print("*"*30)
        except IndexError as e:
            print(str(e))
            print("You must inform the tag from the note")
            sys.exit(1)
  
if arguments[0] == "new":
    try:
        title = arguments[1]
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]

        with open(filepath, 'a') as file_:
            file_.write("\t".join(text) + "\n")

    except IndexError as e:
        print(f"[Error] {str(e)}")
        print("You must give a title to a new note as follows: new title")
        #\t
    