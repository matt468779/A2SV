class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]
        temp = []
        if k == len(num):
            return "0"
            
        for i in range(1, len(num)):
            while stack and num[i] < stack[-1]:
                temp.append(stack.pop())
            stack.append(num[i])

        delete = temp + stack[::-1] 

        for i in range(k):
            num = num.replace(delete[i], '', 1)
        
        for i in range(len(num)-1):
            if num[0] == "0":
                num = num.replace("0", '', 1)
            else:
                break
        
        return num