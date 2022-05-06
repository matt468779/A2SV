class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        last = (len(piles) * 2) // 3 
        count = 0
        for i in range(1, last, 2):
            count += piles[i]

        return count