#!/app/python-base/.venv/bin/python
"""Calculadora Prefix.

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

Os resultados serão salvos em "prefixcalc.log"
"""
__version__ = "0.1.1"
import os
import sys
import logging
from datetime import datetime
#log
log_level = os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger("teste", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
#formatação
fmt = logging.Formatter(
    "%(asctime)s\t%(name)s\t%(levelname)s\t"
    "l:%(lineno)d\tf:%(filename)s:\t%(message)s"
)

ch.setFormatter(fmt)
log.addHandler(ch)

while True:
    arguments = sys.argv[1:]

    #validação
    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    #validação
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", 'div')
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            print(f"Numero inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)

#TODO: usar dict de func
    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv("USER", "Anonymous")

    print(f"O resultado é {result}")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        log.error("You don't have permission to acess this path %s", str(e))
        sys.exit(1)
    
    if input("pressione enter para continuar ou qualquer tecla para sair: "):
        break
