class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zeros = []
        length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            if len(zeros) > k:
                start = zeros.pop(0) + 1
            length = max(length, i - start + 1)
        return length