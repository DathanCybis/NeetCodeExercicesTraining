# Group Anagrams (Versão simplificada)
# Dado um array de strings, agrupá-las por anagramas.
# Saída: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

entrada = ["eat", "tea", "tan", "ate", "nat", "bat"]
dicio = {}

for palavra in entrada:
    alfabeto = [0] * 26
    for letra in palavra:
        alfabeto[ord(letra) - ord('a')] += 1
    
    chave = tuple(alfabeto)

    if chave not in dicio:
        dicio[chave] = []
    dicio[chave].append(palavra)

print(list(dicio.values()))
