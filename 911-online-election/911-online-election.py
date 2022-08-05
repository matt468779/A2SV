class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        voteCount = {persons[0]:1}
        self.leading = [persons[0]]
        for p in persons[1:]:
            if p in voteCount:
                voteCount[p] += 1
            else:
                voteCount[p] = 1
            if voteCount[p] >= voteCount[self.leading[-1]]:
                self.leading.append(p)
            else:
                self.leading.append(self.leading[-1])
        print(self.leading)
                
    def q(self, t: int) -> int:
        lo = 0
        hi = len(self.leading)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.times[mid] == t:
                return self.leading[mid]
            elif self.times[mid] > t:
                hi = mid-1
            else:
                lo = mid+1
        return self.leading[lo-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)