class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime = 0
        waitTimeSum = 0
        for arriveTime, prepTime in customers:
            currTime = max(arriveTime, currTime)
            currTime += prepTime
            waitTimeSum += (currTime - arriveTime)
        return waitTimeSum/len(customers)

        