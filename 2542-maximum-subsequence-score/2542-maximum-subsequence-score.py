class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        nums1_copy = list(nums1)
        for i in range(len(nums2)):
            nums1[i] = (-nums1[i], i)            
            nums2[i] = (nums2[i], i)
        
        heapq.heapify(nums1)
        heapq.heapify(nums2)
        
        visited = [False] * len(nums1)
        total = 0
        for _ in range(k-1):
            num, index = heapq.heappop(nums1)
            total -= num
            visited[index] = True
        
        while nums1 and nums2:
            num, index = heapq.heappop(nums2)
            if visited[index]:
                temp_num, temp_index = heapq.heappop(nums1)
                while nums1 and visited[temp_index]:
                    temp_num, temp_index = heapq.heappop(nums1)
                
                if visited[temp_index]:
                    break
                    
                visited[temp_index] = True
                total -= temp_num
            else:
                visited[index] = True
                total += nums1_copy[index]
                
            res = max(res, total * num)
            total -= nums1_copy[index]
        
        return res