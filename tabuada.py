#!/app/python-base/.venv/bin/python
"""Imprime a tabuada do 1 ao 10"""
__version__="0.1.1"
__author__="Andre Luiz Goncalves"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

base = list(range(1, 11))
for n1 in base:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in base:  
        resultado = n1 * n2    
        print("{:-^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18, "\n")
