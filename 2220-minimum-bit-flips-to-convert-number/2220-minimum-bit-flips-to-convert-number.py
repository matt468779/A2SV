class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        while start or goal:
            lastStart = start & 1
            lastGoal = goal & 1
            
            res += lastStart ^ lastGoal
            
            start >>= 1
            goal >>= 1
        
        return res