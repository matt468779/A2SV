class Solution:
    def maximumRequestsUtil(self, requests, buildings , currentIndex):
        if currentIndex == len(requests):
            return 0 if min(buildings) == 0 and max(buildings) == 0  else -999999
        
        source,destination = requests[currentIndex]
        buildings[source] -= 1
        buildings[destination] += 1
        result = 1 + self.maximumRequestsUtil(requests,buildings,currentIndex+1)

        buildings[source] += 1
        buildings[destination] -= 1
        
        result = max(result,self.maximumRequestsUtil(requests,buildings,currentIndex+1))
        return result
        
        
        
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        buildings = [0 for _ in range(n)]
        return self.maximumRequestsUtil(requests,buildings,0)