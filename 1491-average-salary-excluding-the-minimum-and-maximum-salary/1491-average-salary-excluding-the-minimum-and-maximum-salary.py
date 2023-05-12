class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = float('-inf')
        minSalary = float('inf')
        totSalary = 0
        for sal in salary:
            maxSalary = max(maxSalary, sal)
            minSalary = min(minSalary, sal)
            totSalary += sal
        
        return (totSalary-minSalary-maxSalary) / (len(salary)-2)