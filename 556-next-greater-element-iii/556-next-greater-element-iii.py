class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        s = []
        for i in range(len(n)-1, -1, -1):
            while s and n[i] >= n[s[-1]]:
                s.pop()
            s.append(i)
            if len(s) > 1:
                for i in range(s[0]+1, len(n)):
                    if n[i] > n[s[1]] and n[i] < n[s[0]]:
                        s[0] = i
                n = n[:s[1]] + n[s[0]] + n[s[1]+1:s[0]] + n[s[1]] + n[s[0]+1:]
                temp = ""
                for char in sorted(n[s[1]+1:]):
                    temp = temp + char
                n = int(n[:s[1]+1] + temp) 
                if n <= 2147483647:
                    return n
                break
        return -1