class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_dict = {}
        for num in nums:
            digit_sum = sum(map(int, (str(num))))
            if digit_sum not in digit_sum_dict:
                digit_sum_dict[digit_sum] = []
            heapq.heappush(digit_sum_dict[digit_sum], -num)
        
        res = -1
        for i in digit_sum_dict:
            if len(digit_sum_dict[i]) > 1:
                s = -heapq.heappop(digit_sum_dict[i])
                s += -heapq.heappop(digit_sum_dict[i])
                res = max(res, s)
        
        return res