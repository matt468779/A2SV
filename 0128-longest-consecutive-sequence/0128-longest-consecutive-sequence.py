class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res, length = 0, 0
        for num in nums:
            if num in numSet:
                length = 1
                left = num-1
                while left in numSet:
                    length += 1
                    numSet.remove(left)
                    left -= 1
                
                right = num+1
                while right in numSet:
                    length += 1
                    numSet.remove(right)
                    right += 1
            res = max(res, length)
            
        return res