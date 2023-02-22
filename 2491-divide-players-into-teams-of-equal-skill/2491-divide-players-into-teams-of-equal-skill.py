class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        valid_sum = skill[0] + skill[-1]
        l, r = 0, len(skill)-1
        chemistry = 0

        while l < r:
            curr_sum = skill[l] + skill[r]
            if curr_sum != valid_sum:
                return -1
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        return chemistry