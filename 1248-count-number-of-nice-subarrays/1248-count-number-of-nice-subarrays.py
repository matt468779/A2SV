class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odds = [-1]
        for i in range(len(nums)):
            if nums[i] % 2:
                odds.append(i)
              
        odds.append(len(nums))
        for i in range(1, len(odds)-k):
            count += (odds[i] - odds[i-1]) * (odds[i+k] - odds[i+k-1])
            
        return count
                
                
                
            
        
        