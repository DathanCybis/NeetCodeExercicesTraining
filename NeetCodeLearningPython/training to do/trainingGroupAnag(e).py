# Saber se duas palavras são anagramas
# Entrada: "amor", "roma"
# Saída esperada: True

palavra1 = 'amor'
palavra2 = 'roma'
visto = {}
visto2 = {}

for letra in palavra1:
    if letra in visto:
        visto[letra] +=1
    else:
        visto[letra] = 1

print(visto)

for letra in palavra2:
    if letra in visto2:
        visto2[letra] += 1
    else:
        visto2[letra] = 1

print(visto2)

print(visto == visto2)