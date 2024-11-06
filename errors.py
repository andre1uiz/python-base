#!/app/python-base/.venv/bin/python
"""
tratamento de erros precisa ser especificos
"""
import os
import sys

# Look before you leap (LBYP)
#EAFP Easy to ask forgiveness than permission

try:
    names = open("names.txt").readlines() #FileNotFoundError
    1/0 #ZeroDivisionError
    print(names.banana) #AtributeError
#except: #Bare except - irá para esta rotina em todos os erros possiveis
except FileNotFoundError as e:
    print(f"[Error] {str(e)}.")
    sys.exit(1)
try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    #TODO: usar retry
