class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = []
        def backtrack(indx,word):
            if indx >= len(arr):
                res.append(word)
                return
            add = arr[indx]
            backtrack(indx+1,word+add)
            backtrack(indx+1,word)
        backtrack(0,"")
        ans = 0
        for word in res:
            container = []
            for i in range(len(word)):
                if word[i] in container:
                    break
                else:
                    if i != len(word)-1:
                        container.append(word[i])
                    else:
                        ans = max(ans, len(word))
        return ans