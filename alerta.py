#!/app/python-base/.venv/bin/python
"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice
de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo
das condições:

temp maior que 45: ALERTA!!! Perigo calor extremo
temp x 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp < 0: ALERTA: Frio extremo
"""
__version__ = "0.1.0"
import sys
import logging

log  = logging.Logger("alerta")

info = {
    "temp" : None,
    "umidity" : None,
}

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Informe o valor de {key} ").strip())    
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temp"]
umidity = info["umidity"]
if temp > 45:
    print("ALERTA!!! Perigo calor extremo \U0001F975")
elif temp * 3 >= umidity:
    print("ALERTA!!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Temperatura normal \U0001F60E")
elif temp < 10 and temp > 0:
    print("Frio ")
elif temp < 0:
    print("ALERTA: Frio extremo \U0001F976")
