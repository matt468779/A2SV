class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = deque()
        j = 0
        
        for i in range(len(nums1)):  
            if (nums3 and j < n and nums3[0] > nums2[j]) or ((not nums3) and j < n and i < m and nums1[i] > nums2[j]):
                if i < m:
                    nums3.append(nums1[i])
                nums1[i] = nums2[j]
                j += 1
            elif nums3:
                if i < m:
                    nums3.append(nums1[i])
                nums1[i] = nums3.popleft()
            elif i >= m and j < n:
                nums1[i] = nums2[j]
                j += 1
