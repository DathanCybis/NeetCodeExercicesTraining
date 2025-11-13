# Inverter um dicionário
# Entrada: {'a': 1, 'b': 2, 'c': 3}
# Saída esperada: {1: 'a', 2: 'b', 3: 'c'}

normal = {'a': 1, 'b': 2, 'c': 3}
invertido = {}

for i, v in normal.items():
    invertido[v] = i

print(invertido)
