class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums)-1
        mid = (lo+hi)//2

        while lo < hi:
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
            mid = (lo+hi)//2

        if mid < len(nums) and mid > -1 and nums[mid] == target:
            res = []
            i = mid-1
            while i > -1 and nums[i] == target:
                i -= 1
            res.append(i+1)
            
            i = mid+1
            while i < len(nums) and nums[i] == target:
                i += 1
            res.append(i-1)
            return res
        return [-1, -1]