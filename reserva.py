#!/app/python-base/.venv/bin/python
"""
Faça um programa de terminal que exibe ao usuário uma lista de quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`
#código, nome, preço
1, Master Suite, 500
2, Quarto Familia, 200
3, Quarto Single, 100
4, Quarto Simples, 50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`

```
#cliente, quarto, dias
Bruno, 3, 12
```

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.

"""
__version__ = "0.1.0"

import logging
import sys
import os
from datetime import datetime
#log
log_level = os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger("reserva", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
#formatação
fmt = logging.Formatter(
    "%(asctime)s\t%(name)s\t%(levelname)s\t"
    "l:%(lineno)d\tf:%(filename)s:\t%(message)s"
)

ch.setFormatter(fmt)
log.addHandler(ch)


rooms = {}
reserved = []

print(
    "Reserva de Quartos\n"
     +"Código\t|\tDescrição\t|\tPreço\t\t|\tDisponibilidade\n")

for room in open("reservas.txt", "r"):
    try:
        reserved.append(int(room.split(",")[1].strip()))  
    except IndexError:
        break

try:
    for room in open("quartos.txt", "r").readlines():
        code, name, price = room.split(',')
        rooms[int(code)]= {
            "name" : name,
            "price": float(price), #TODO: Decimal
        }
        is_available = "\U00002612" if int(code) in set(reserved) else "\U00002611"
        print(f'{code}\t|\t{name}\t|\tR$ {float(price):.2f}\t|\t{is_available}')
except Exception as e:
    log.error(f"Falha no arquivo de quartos.txt {str(e)}")

name = input("Informe o nome: ").strip()

try:
    room_number = int(input("Informe o número do quarto para locação: ").strip())
except ValueError:
    log.error("Valor incorreto, você deve inserir o número do quarto")
    sys.exit(1)

try:
    days = int(input("informe o número de dias para reserva: ").strip())
except ValueError:
    log.error("A quantidade de dias deve ser um valor inteiro")
    sys.exit(1)

if int(room_number) in set(reserved):
    print("Desculpe, este quarto já foi reservado")
else:
    try:
        final_value = float(rooms[room_number]["price"]) * days
    except KeyError:
        print("Desculpe, o quarto selecionado não existe.")
        sys.exit(1)
    try:
        with open("reservas.txt","a") as reserve:
            reserve.write(f"{name}, {room_number}, {days}\n")
            print(f"{rooms[room_number]["name"]} reservado por {days} dias a um valor final de R${final_value:.2f}")
    except:
            log.error("Falha ao escrever o arquivo, reserva não efetivada")




