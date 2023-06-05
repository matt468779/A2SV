class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def getNum(s):
            res = 0
            for num in s:
                res = res*10 + ord(num)-ord('0')
            
            return res
        
        res = getNum(num1) * getNum(num2)
        
        res_str = deque()
        while res:
            n = res % 10
            res = res // 10
            res_str.appendleft(chr(ord('0') + n))
        
        return ''.join(res_str) if res_str else '0'
        