#!/app/python-base/.venv/bin/python
"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras
e imprime cada uma delas com as vogais duplicadas.

ex:
`python repete_vogal.py`
'Digite uma palavra ou enter para sair: 'python''
'Digite uma palavra ou enter para sair: 'Bruno''
'Digite uma palavra ou enter para sair: <enter>'
pythoon
Bruunoo
"""
import logging
import sys

words = []
duplicate = []
vowels = "aeiou"

while True:
    
    word = input("Digite uma palavra ou enter para sair: ").strip()
    if word:
        words.append(word)
    else:
        break

for word in words:
    new_word = ""
    for letter in word:
        #TODO: Remover acentuação usando função
        if letter.lower() in vowels:
            new_word = new_word + letter * 2
        else:
            new_word = new_word + letter
    duplicate.append(new_word)

# for word in duplicate:
#     print(word)

print(*duplicate, sep="\n") #mesma funçã odo for anterior operador unário '*' para listas 