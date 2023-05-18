class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        isEvenIndex = True
        while n:
            if isEvenIndex:
                even += 1 & n
            else:
                odd += 1 & n
            n >>= 1
            isEvenIndex = not isEvenIndex
        
        return [even, odd]