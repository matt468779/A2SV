class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        res = 0
        nums.append(0)
        
        for i in range(len(nums)-1):
            nums[i] += nums[i-1]
        
        for i in range(len(nums) - firstLen):
            firSum = nums[i+firstLen-1] - nums[i-1]
            for j in range(i-secondLen+1):
                secSum = nums[j+secondLen-1] - nums[j-1]
                res = max(res, firSum+secSum)

            for j in range(i+firstLen, len(nums)-secondLen):
                secSum = nums[j+secondLen-1] - nums[j-1]
                res = max(res, firSum+secSum)

        return res
                    