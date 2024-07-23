class Solution:
    def isPathCrossing(self, path: str) -> bool:
        keyx,keyy = 0,0
        cor = {(keyx,keyy): 1}
        for i in path:
            if i == "N":
                keyy += 1
            elif i == "E":
                keyx += 1
            elif i == "S":
                keyy -= 1
            elif i == "W":
                keyx -= 1
            
            if (keyx,keyy) in cor:
                return True
            else:
                cor[(keyx,keyy)] = 1
        return False