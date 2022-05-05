class Solution:
    def checkArithmeticInterval(self, nums: List[int]):
        if len(nums) > 1:
            nums.sort()
            d = nums[1] - nums[0]
            for i in range(2, len(nums)):
                if nums[i] - nums[i-1] != d:
                    return False
            return True

        else:
            return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            answer.append(self.checkArithmeticInterval(nums[l[i]:r[i]+1]))
        return answer