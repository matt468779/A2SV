class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        maxList = {nums2[-1]: -1}

        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] < nums2[i+1]:
                maxList[nums2[i]] = nums2[i+1]
            else:
                max = maxList[nums2[i+1]]
                while max > -1 and nums2[i] > max:
                    max = maxList[max]
                maxList[nums2[i]] = max

        for i in range(len(nums1)):
            nums1[i] = maxList[nums1[i]]    
        
        return nums1