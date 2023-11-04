class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def combination(cur,n):
            if len(cur) == 2*n:
                res.append(cur)
                return
            cur.append(")")
            combination(cur[::],n)
            cur.pop()
            cur.append("(")
            combination(cur[::],n)
        combination([],n)
        
        ans = []
        for parentheses in res:
            stack = []
            well_formed = True
            for par in parentheses:
                if par == "(":
                    stack.append("(")
                else:
                    if stack:
                        stack.pop()
                    else:
                        well_formed = False
                        break
            if well_formed and stack == []:
                stri = "".join(parentheses)
                ans.append(stri)
            
        return ans
            
        