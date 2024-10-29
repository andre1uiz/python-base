#!/app/python-base/.venv/bin/python
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que 
frequentam cada uma das atividades.
"""
__version__ = "0.1.2"
#Dados
alunos = {
"Sala 1" : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
"Sala 2" : ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Sofia", "Joana", "Antonio"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {"Inglês" : aula_ingles,
              "Música" : aula_musica, 
              "Dança" : aula_danca,}

# Listar alunos em cada atividade por sala
#continuar exercicio aqui para listar as salar com  dicts
for sala, alunos_sala in alunos.items():
    print(f"Atividades alunos {sala}:")
    for aula, alunos_aula in atividades.items():
        atividades_sala = set(alunos_sala) & set(alunos_aula)
        print(f"{aula}: {atividades_sala}")
    print("+"*40)
