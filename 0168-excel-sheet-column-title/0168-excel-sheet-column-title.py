class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = deque()
        ord_A = ord('A')
        while columnNumber:
            columnNumber -= 1
            rem = columnNumber % 26
            res.appendleft(chr(ord_A + rem))
            columnNumber //= 26
            
        return ''.join(res)
    