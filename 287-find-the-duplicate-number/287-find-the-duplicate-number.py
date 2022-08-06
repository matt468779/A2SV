class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 1
        hi = len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            
            if count > mid:
                hi = mid
            else:
                lo = mid+1
        return lo