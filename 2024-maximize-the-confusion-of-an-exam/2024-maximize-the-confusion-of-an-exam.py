class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maximizeChar(char, oppChar):
            l, r = 0, 0
            res = 0
            kk = k

            while r < len(answerKey):
                if answerKey[r] == char:
                    r += 1
                elif kk > 0:
                    r += 1
                    kk -= 1
                else:
                    if answerKey[l] == oppChar:
                        kk += 1
                    l += 1

                res = max(res, r-l)
            
            return res
        return max(maximizeChar('T', 'F'), maximizeChar('F', 'T'))