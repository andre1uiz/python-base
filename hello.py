#!/usr/local/bin/python python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
"""
__version__="0.0.1"
__author__="André Luiz Gonçalves"
__license__="Unlicensed"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = 'Hello, World!'

if current_language == 'pt_BR':
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)