nums = [3,4,5,6]
alvo = 7
vistos = {}

for i, n in enumerate(nums):
    diff = alvo - n
    if diff in vistos:
        print([vistos[diff], i])
    vistos[n] = i
