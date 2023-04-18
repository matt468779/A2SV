class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        presum = [0] * 52
        for start, end in ranges:
            presum[start] += 1
            presum[end+1] -= 1
        
        for i in range(1, len(presum)):
            presum[i] += presum[i-1]
            
        for i in range(left, right+1):
            if presum[i] == 0:
                return False
        
        return True