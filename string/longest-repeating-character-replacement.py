class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longestCount = 0
        left = 0
        maxCount = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxCount = max(maxCount, count[s[right]])
            while (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1
            longestCount = max(longestCount, right - left + 1)
        return longestCount
        