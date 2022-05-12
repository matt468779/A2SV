class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        i = 0
        equ = []
        while i < len(s):
            if s[i] == '+' or s[i] == '*' or s[i] == '/':#1+2-322+53
                equ.append(s[i])
                i += 1
            elif s[i] == '-':
                num = self.extractNumber(s[i+1:])
                equ.append('+')
                equ.append('-'+num)
                i += 1 + len(num)
            else:
                num = self.extractNumber(s[i:])
                equ.append(num)
                i += len(num)
        stack = []
        i = 0
        while i < len(equ):
            if equ[i] == '*':
                stack.append(int(stack.pop())*int(equ[i+1]))
                i+=2
            elif equ[i] == '/':
                num = int(stack.pop())
                res = num//int(equ[i+1]) if num >= 0 else -(-num//int(equ[i+1]))
                stack.append(res)
                i+=2
            else:
                stack.append(equ[i])
                i+=1
        result = 0
        for i in range(0, len(stack), 2):
            result += int(stack[i])

        return result

    def extractNumber(self, exp: str) -> str:
        num = ''
        for e in exp:
            if e == '+' or e == '*' or e == '/' or e == '-':
                break
            num += e
        return num