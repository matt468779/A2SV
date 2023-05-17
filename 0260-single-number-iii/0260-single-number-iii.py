class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        theTwoLeft = 0
        for num in nums:
            theTwoLeft ^= num

        mask = 1
        while not mask & theTwoLeft:
            mask *= 2

        group0, group1 = 0, 0
        for num in nums:
            if num & mask:
                group1 ^= num
            else:
                group0 ^= num

        return [group0, group1]