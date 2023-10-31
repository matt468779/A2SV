class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indDict = defaultdict(list)
        for i in range(len(nums)):
            indDict[nums[i]].append(i)
        
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff == nums[i] and len(indDict[diff]) > 1:
                return indDict[diff][:2]
            elif diff != nums[i] and diff in indDict:
                return [indDict[nums[i]][0], indDict[diff][0]]
        
        return [0, 1]