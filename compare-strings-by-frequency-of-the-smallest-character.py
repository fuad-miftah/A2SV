class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda x: x.count(min(x))
        words = sorted(list(map(f, words)))
        res = []
        for i in map(f,queries):
            res.append(len(words)-bisect_right(words,i))
        return res