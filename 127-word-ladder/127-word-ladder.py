class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = set([beginWord])
        q2 = set()
        visited = set()
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                popped = q.pop()
                if popped in visited:
                    continue
                if popped == endWord:
                    return res
                for i in range(len(popped)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        temp = popped[:i] + j + popped[i+1:]
                        if temp not in visited and temp in words and temp not in q:
                            q2.add(temp)
                visited.add(popped)
            q = q2
            q2 = set()
        return 0