class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo+1 < hi:
            mid = (lo+hi)//2
            print(mid)
            if nums[lo] < nums[mid]:
                lo = mid
            else:
                hi = mid
        br = 0
        if nums[lo] > nums[hi]:
            br = hi
            nums = nums[hi:] + nums[0:hi]

        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return (mid + br) % len(nums)
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
                