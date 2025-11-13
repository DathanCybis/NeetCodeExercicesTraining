# Quantas vezes cada palavra aparece
# Entrada: "o rato roeu a roupa do rei de roma"
# Saída esperada: {'o': 2, 'rato': 1, 'roeu': 1, 'a': 1, 'roupa': 1, 'do': 1, 'rei': 1, 'de': 1, 'roma': 1}

palavra = "o rato roeu a roupa do rei de roma".split()
palavras = {}

for i, v in enumerate(palavra):
    if v in palavras:
        palavras[v] += 1
    else:
        palavras[v] = 1

print(palavras)
