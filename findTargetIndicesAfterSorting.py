class Solution:
    def targetIndices(self, nums, target: int):
        index = 0
        count = 0
        for num in nums:
            if target > num:
                index += 1
            elif target == num:
                count += 1
        result = []
        for i in range(index, index+count):
            result.append(i)
        return result
