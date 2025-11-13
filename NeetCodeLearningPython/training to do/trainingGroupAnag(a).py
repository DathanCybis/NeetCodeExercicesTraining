#Contar letras de uma palavra
#Entrada: "banana"
#Saída esperada: {'b': 1, 'a': 3, 'n': 2}

palavra = 'banana'
letras = {}

for letra in palavra:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1
        
print(letras)