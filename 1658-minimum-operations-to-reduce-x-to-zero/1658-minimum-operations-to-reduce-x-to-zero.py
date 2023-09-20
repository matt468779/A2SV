class Solution(object):
    def minOperations(self, nums, x):
        total_sum = sum(nums)
        max_length = -1
        curr_sum = 0
        count_left = 0

        for right_pointer in range(len(nums)):
            curr_sum += nums[right_pointer]
            while count_left <= right_pointer and curr_sum > total_sum - x:
                curr_sum -= nums[count_left]
                count_left += 1
            if curr_sum == total_sum - x:
                max_length = max(max_length, right_pointer - count_left + 1)

        return -1 if max_length == -1 else len(nums) - max_length