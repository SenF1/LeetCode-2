class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = True
        idx = 1
        while time > 0:
            if direction:
                idx += 1
                if idx == n:
                    direction = not direction
            else:
                idx -= 1
                if idx == 1:
                    direction = not direction
            time -= 1
        return idx