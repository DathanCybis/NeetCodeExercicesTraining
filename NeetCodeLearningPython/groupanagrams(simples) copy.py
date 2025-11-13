# Group Anagrams (Versão simplificada)
# Dado um array de strings, agrupá-las por anagramas.
# Saída: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

entrada = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = {}

for s in entrada:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1

    chave = tuple(count)

    if chave not in res:
        res[chave] = []
    res[chave].append(s)
saida = list(res.values())
print(saida)
