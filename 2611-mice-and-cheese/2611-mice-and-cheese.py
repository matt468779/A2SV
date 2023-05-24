class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        res = 0
        diff = []
        for i in range(len(reward1)):
            diff.append((reward1[i] - reward2[i], i))
        
        diff.sort(key=lambda x: abs(x[0]), reverse=True)
        
        k2 = len(reward1)-k
        for i in range(len(diff)):
            if k2 == 0 or k > 0 and diff[i][0] >= 0:
                res += reward1[diff[i][1]]
                k -= 1
            elif k == 0 or diff[i][0] <= 0:
                res += reward2[diff[i][1]]
                k2 -= 1
            
        return res