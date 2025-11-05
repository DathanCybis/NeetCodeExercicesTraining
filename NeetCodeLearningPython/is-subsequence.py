s="node"
t="neetcode"
vistos = []

for i in s:
    if i not in t:
        print("False") #return False
        break
    vistos.append(i)
print()

for i, v in enumerate(s):
    print(i, v)
    if v in t:
        print("ok")

#print(vistos)