#!/app/python-base/.venv/bin/python
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

    ou informe através da CLI argument '--lang'
    Ou o usuário terá que digitar

Execução:

    python3 hello.py
    ./hello.py
"""
__version__="0.1.4"
__author__="André Luiz Gonçalves"
__license__="Unlicensed"

import os
import sys
import logging

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

arguments = {"lang" : None, 
             "count" : 1,
             }

for arg in sys.argv[1:]:
    #TODO: tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try '--key=value: %s",
             arg, str(e)
        )
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()

    #validation
    if key not in arguments:
        print(f"Invalid option {key}")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO: usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "Choose your language: "
        )
current_language = current_language[:5]

msg = {"en_US" : 'Hello, World!',
       'pt_BR' : "Olá, Mundo!",
       "it_IT" : "Ciao, Mundo!",
       "es_SP" :  "Hola, Mundo!",
       "fr_FR" : "Bonjour Monde!"
       }

#O(1) Nível de complexidade
#Solução sem tratamento de erros 
#message = msg.get(current_language, "en_US")

#EAFP solução com tratamento
try:
    message = msg[current_language]

except KeyError as e:
    print(f"[Error] {str(e)}")
    print(f"Language is invalid, choose from {list(msg.keys())}")
    sys.exit(1)

