"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def traverse(self,indx,employees,visited):
        if employees[indx].subordinates == []:
            self.output += employees[indx].importance
            return
        if indx in visited:
            return
        visited.add(indx)
        self.output += employees[indx].importance
        for i in range(len(employees[indx].subordinates)):
            nindx = -1
            for j in range(len(employees)):
                if employees[j].id == employees[indx].subordinates[i]:
                    nindx = j
                    break

            self.traverse(nindx,employees,visited)
        return

    def getImportance(self, employees: List['Employee'], id: int) -> int:

        indx = -1
        for i in range(len(employees)):
            if employees[i].id == id:
                indx = i
                break

        self.output = 0
        self.traverse(indx,employees,set())
        return self.output