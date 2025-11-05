class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visto = {}
        for i in s:
            if i in visto:
                visto[i] += 1
            else:
                visto[i] = 1

        for i in t:
            if i in visto:
                visto[i] -= 1
        cont = 0
        for i in visto:
            if visto[i] == 0:
                cont+=1

        if cont == len(visto):
            return True
        else:
            return False
        
print(Solution().isAnagram("racecar", "carrace"))
