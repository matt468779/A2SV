class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [0] * (len(ratings)+1)
        ratings.append(float('inf'))
        ratings_copy = list(ratings)
        for i in range(len(ratings)):
            ratings_copy[i] = (ratings_copy[i], i)
            
        heapq.heapify(ratings_copy)
        while len(ratings_copy) > 1:
            rating, ind = heapq.heappop(ratings_copy)
            if ratings[ind-1] >= rating <= ratings[ind+1]:
                res[ind] = 1
            else:
                if ratings[ind-1] < rating:
                    res[ind] = max(res[ind], res[ind-1]+1)
                if ratings[ind+1] < rating:
                    res[ind] = max(res[ind], res[ind+1]+1)

        return sum(res)