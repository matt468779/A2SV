class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(lst, start, end):
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1
                
        str_lst = list(s)
        for i in range(0, len(s), 2*k):
            reverse(str_lst, i, min(i+k-1, len(s)-1))
        
        return ''.join(str_lst)