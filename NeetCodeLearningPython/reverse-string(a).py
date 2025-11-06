from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s), 0, -1):
            s.append(s[i-1])
        for i in range(int(len(s)/2)):
            s.remove(s[i])
        

# Testando
#s = ["n","e","e","t"]
s = ["r","a","c","e","c","a","r"]
Solution().reverseString(s)
print(s)
