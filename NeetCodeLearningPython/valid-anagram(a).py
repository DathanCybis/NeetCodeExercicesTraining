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
            else:
                return False
        
        for i in visto:
            if visto[i] != 0:
                return False
            
        return True
        
print(Solution().isAnagram("racecar", "carrace"))
