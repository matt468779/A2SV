class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bin_search(arr, key):
            lo = 0
            hi = len(arr)-1
            while lo <= hi:
                mid = (lo+hi)//2
                if arr[mid] == key:
                    return mid
                elif arr[mid] > key:
                    hi = mid-1
                else:
                    lo = mid+1
            
            return hi
        
        res_r = deque()
        res_l = deque()
        l = bin_search(arr, x)
        r = l+1
        for i in range(k):
            if l < 0 and r < len(arr):
                res_r.append(arr[r])
                r += 1
                continue
            if r >= len(arr) and l > -1:
                res_l.appendleft(arr[l])
                l -= 1
                continue
            
            if abs(arr[l]-x) <= abs(arr[r]-x):
                res_l.appendleft(arr[l])
                l -= 1
            else:
                res_r.append(arr[r])
                r += 1
        
        return res_l + res_r