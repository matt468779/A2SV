class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = 1
        hi = 1000000
        while lo < hi:
            mid = (lo+hi)//2
            s = 0
            for n in nums:
                s += ((n-1)//mid)+1

            if s <= threshold:
                hi = mid
            else:
                lo = mid+1
        return hi