class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        a = {s[0]: True}
        longest = [s[0]]
        length = 1
        for i in range(1, len(s)):
            while s[i] in a.keys():
                a.pop(longest.pop(0))
            longest.append(s[i])
            a[s[i]] = True
            length = max(length, len(longest))
        return length