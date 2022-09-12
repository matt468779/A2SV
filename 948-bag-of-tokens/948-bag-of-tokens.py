class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = collections.deque(sorted(tokens))
        res, score = 0, 0
        while tokens and (score or power >= tokens[0]):
            if power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
            elif score > 0:
                power += tokens.pop()
                score -= 1
            res = max(res, score)

        return res