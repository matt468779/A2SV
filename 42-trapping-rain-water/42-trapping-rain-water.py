class Solution:
    def trap(self, height: List[int]) -> int:
        nextMax = [height[-1]] * len(height)
        prevMax = [height[0]] * len(height)
        res, n = 0, len(height)
        
        for i in range(1, n):
            prevMax[i] = max(height[i], prevMax[i-1])
            nextMax[-i-1] = max(height[-i-1], nextMax[-i])

        for i in range(len(height)):
            res += min(prevMax[i], nextMax[i]) - height[i]
            
        return res
    