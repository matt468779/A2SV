class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(mid):
            i, count = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False

        if p == 0: return 0
        nums.sort()
        l, h = 0, 10**9
        res = 10**9

        while l <= h:
            mid = l + (h - l)//2
            if isValid(mid):
                res = mid
                h = mid - 1
            else:
                l = mid + 1
        return res