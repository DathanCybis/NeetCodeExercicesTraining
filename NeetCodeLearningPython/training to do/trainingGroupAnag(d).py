# Palavras agrupadas por tamanho
# Entrada: ['sol', 'lua', 'estrela', 'mar', 'céu', 'universo']
# Saída esperada: {3: ['sol', 'lua', 'mar', 'céu'], 7: ['estrela'], 8: ['universo']}

palavras = ['sol', 'lua', 'estrela', 'mar', 'céu', 'universo']
grupos = {}

for palavra in palavras:
    j = len(palavra)
    if j not in grupos:
        grupos[j] = []
    grupos[j].append(palavra)

print(grupos)
