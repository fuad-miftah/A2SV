class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        left = 0
        res = 0
        for right,fr in enumerate(fruits):

            d[fr] = right
            if len(d)>2:
                minn = min(d.values())
                del d[fruits[minn]]
                left = minn+1
            res = max(res, right - left + 1)
        return res