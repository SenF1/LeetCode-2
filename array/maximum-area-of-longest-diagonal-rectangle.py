class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longestIdx = 0
        longestLength = -1
        for i in range(len(dimensions)):
            length = math.sqrt(dimensions[i][0]*dimensions[i][0] + dimensions[i][1]*dimensions[i][1])
            if length > longestLength:
                longestIdx = i
                longestLength = length
            elif length == longestLength:
                if dimensions[i][0]*dimensions[i][1] > dimensions[longestIdx][0] * dimensions[longestIdx][1]:
                    longestIdx = i
                    longestLength = length
        return dimensions[longestIdx][0] * dimensions[longestIdx][1]
        