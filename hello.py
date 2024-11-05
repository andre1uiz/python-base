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
__version__="0.1.2"
__author__="André Luiz Gonçalves"
__license__="Unlicensed"

import os
import sys

arguments = {"lang" : None, 
             "count" : 1,
             }

for arg in sys.argv[1:]:
    #TODO tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO usar repetição
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
print(msg[current_language] * int(arguments["count"]))