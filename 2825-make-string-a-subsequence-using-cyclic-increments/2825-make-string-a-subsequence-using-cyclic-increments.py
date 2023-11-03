class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
            
        if len(str1) < len(str2):
            return False

        sec = 0

        for i in range(len(str1)):
            if sec >= len(str2):
                break

            cu1 = ord(str1[i]) - 97
            cu2 = ord(str2[sec]) - 97

            if cu1 == cu2 or  (cu1 + 1) % 26 == cu2:
                sec += 1

        if sec < len(str2):
            return False
        return True
