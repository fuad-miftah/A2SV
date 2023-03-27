class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            res.append(Counter(words[i]))
        
        ans = []
        for i in range(97,97+26):
            minv = 101
            for j in range(len(res)):
                if chr(i) in res[j]:
                    minv = min(minv,res[j][chr(i)])
                    if j == len(res) - 1:
                        for k in range(minv):
                            ans.append(chr(i))
                else:
                    break
        return ans