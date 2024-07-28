class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
        
        left = 0
        right = 0
        min_len = float('inf')
        min_start = 0
        
        char_needed = len(t_map)
        window_map = {}
        
        while right < len(s):
            char = s[right]
            if char in t_map:
                if char in window_map:
                    window_map[char] += 1
                else:
                    window_map[char] = 1
                
                if window_map[char] == t_map[char]:
                    char_needed -= 1
            
            while char_needed == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                char = s[left]
                if char in t_map:
                    window_map[char] -= 1
                    if window_map[char] < t_map[char]:
                        char_needed += 1
                left += 1
            
            right += 1
        
        if min_len == float('inf'):
            return ""
        else:
            return s[min_start:min_start + min_len]
        