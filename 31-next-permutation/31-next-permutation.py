class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = []
        for i in range(len(nums)-1, -1, -1):
            while s and nums[i] >= nums[s[-1]]:
                s.pop()
            s.append(i)
            
            if len(s) >= 2:
                break
        
        if len(s) == 1:
            start, end = 0, len(nums)-1
        else:
            for i in range(s[1]+1, len(nums)):
                if nums[i] > nums[s[1]] and nums[i] <= nums[s[0]]:
                    s[0] = i

            start, end = s[1]+1, len(nums)-1
            nums[s[0]], nums[s[1]] = nums[s[1]], nums[s[0]]

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
