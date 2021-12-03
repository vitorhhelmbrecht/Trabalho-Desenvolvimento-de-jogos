import random
import json


file = open("Tempos.txt", "r")
content = file.read()
linhas = content.splitlines()
tempos = []
for linha in linhas:
    tempos.append(linha)

tempoAnterior = 0.00
print('[')
for index, content in enumerate(tempos):
    tempoAtual = float(content)
    print(json.dumps(
        {
            "name": index,
            "delay": tempoAtual - tempoAnterior,
            "line": random.randint(1, 4),
            "type": 1,
            "tempo": tempoAtual
        }) + ', ')
    tempoAnterior = tempoAtual
print(']')
