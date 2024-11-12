#!/app/python-base/.venv/bin/python
"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python numeros_pares.py`
2
4
6
8
...
"""
__version__ = "0.1.0"

for number in range(1,201):
    if number % 2 == 0:
        print(number)