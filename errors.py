#!/app/python-base/.venv/bin/python
"""
"""
import os
import sys

# Look before you leap (LBYP)

if os.path.exists("names.txt"):
    #Race condition
    input("...")
    names = open("names.txt").readlines()
else:
    print("[Error file names.txt not found]")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")