class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        temp = 1
        nums.append("h")
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                temp += 1 
            elif nums[i] != nums[i+1] and temp > 1:
                for j in range(1, temp):
                    count+=j
                temp = 1
        return count