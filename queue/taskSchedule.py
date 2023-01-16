import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        count = collections.Counter(tasks)
        


tasks = ["A","A","A","B","B","B"]
sol = Solution()
sol.leastInterval(tasks,2)