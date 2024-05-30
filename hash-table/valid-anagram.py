class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sd = dict()
        td = dict()
        for c in s:
            if c in sd:
                sd[c] += 1
            else:
                sd[c] = 1
        
        for c in t:
            if c in td:
                td[c] += 1
            else:
                td[c] = 1
        
        for key in sd:
            if key not in td or sd[key] != td[key]:
                return False
        
        return True

        