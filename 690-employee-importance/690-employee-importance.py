"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = {}
        for employee in employees:
            emps[employee.id] = employee
        
        def findImportance(emps, id: int) -> int:
            s = emps[id].importance
            for sub in emps[id].subordinates:
                s += findImportance(emps, sub)
            return s
        return findImportance(emps, id)