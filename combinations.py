class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i,num):
            if len(num) == k:
                res.append(num.copy())
                return
            if i > n:
                return
            num.append(i)
            backtrack(i+1,num.copy())
            num.pop()
            backtrack(i+1,num.copy())
        backtrack(1,[])
        return res