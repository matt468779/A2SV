class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        a = []
        for i in range(len(indices)):
            a.append([indices[i], sources[i], targets[i]]) 
        a.sort()
        
        for i in range(len(a)):
            indices[i] = a[i][0]
            sources[i] = a[i][1]
            targets[i] = a[i][2]

        length = 0
        j = 0
        for i in indices:
            currentIndex = i+length
            if s[currentIndex : currentIndex+len(sources[j])] == sources[j]:
                s = s[:currentIndex] + s[currentIndex:].replace(sources[j], targets[j], 1)
                length += len(targets[j]) - len(sources[j])
            j += 1
        return s