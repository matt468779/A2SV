class Solution:
    def partitionString(self, s: str) -> int:
        sett = set()
        count = 1

        for i in s:
            if i in sett:
                count += 1
                sett = set()

            sett.add(i)

        return count