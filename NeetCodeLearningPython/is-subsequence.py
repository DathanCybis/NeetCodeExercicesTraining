s="node"
t="neetcode"

i = j = 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1

print(i == len(s))










# s="node"
# t="neetcode"
# vistos = []

# for i in s:
#     if i not in t:
#         print("False") #return False
#         break
#     vistos.append(i)
# print()

# for i, v in enumerate(s):
#     if v not in t:
#         print("False") #return False
#         break

#     print(i, v)
#     if v in t:
#         #print("ok")
#         pass

# #print(vistos)