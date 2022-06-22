class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        freq = {}
        for i in range(len(nums)):
            if freq.get(nums[i], -1) == -1:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
                
        freqList = []
        for key in freq.keys():
            heapq.heappush(freqList, (-freq[key], key))
        
        for _ in range(k):
            answer.append(heapq.heappop(freqList)[1])
        
        return answer