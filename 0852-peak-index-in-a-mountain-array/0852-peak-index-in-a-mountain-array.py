class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l+r)//2
            if mid-1 >= 0 and arr[mid-1] < arr[mid]:
                l = mid+1
            elif mid-1 < 0 and arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid-1
        
        return r