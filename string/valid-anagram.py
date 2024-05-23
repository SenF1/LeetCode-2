from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(lambda: 0)
        for v in s:
            dic[v] += 1
        
        for v in t:
            dic[v] -= 1
        
        for value in dic.values():
            if value != 0:
                return False
        return True
        