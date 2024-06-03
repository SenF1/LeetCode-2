class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        result = list(d.keys())[:k]
        return result       