class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        j = len(nums) - 2
        i = len(nums) - 1
        remain = k

        while i > 0 and j >= 0:
            while remain > 0 and j >= 0:
                remain -= nums[i] - nums[j]
                j -= 1
                
            if remain < 0:
                remain = remain + nums[i] - nums[j+1]
                count = i-j-2
            else:
                remain = 0
                count = i-j-1

            remain += count*(nums[i]-nums[i-1])
            j = i-count-1
            res = max(res, count + 1)
            i -= 1

        return res
            