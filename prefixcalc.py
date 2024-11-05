#!/app/python-base/.venv/bin/python
"""Calculadora prefix
Exercicio feito, correção e seguimento do
conteúdo em "prefix_corrigido.py"
Funcionamento:
[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5 
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "André Luiz Gonçalves"
__license__ = "unlicensed"

import sys

arguments = {"operation" : None, "n1" : None, "n2" : None}

operations = ("sum", "sub", "mul", "div")

#for args in sys.argv[1:4]:
#   print(args)

if len(sys.argv) >= 4:
    arguments["operation"] = sys.argv[1].strip()
    arguments["n1"] = float(sys.argv[2])
    arguments["n2"] = float(sys.argv[3])
else:
    arguments["operation"] = input("operação: ").strip()
    arguments["n1"] = float(input("n1: "))
    arguments["n2"] = float(input("n2: "))


def calculate(op, n1, n2):
    if op == "sum":
        return n1 + n2
    elif op == "sub":
        return n1 - n2
    elif op == "mul":
        return n1 * n2
    elif op == "div":
        return n1 / n2


if arguments["operation"] in operations:
    print(calculate(arguments["operation"], arguments["n1"], arguments["n2"]))