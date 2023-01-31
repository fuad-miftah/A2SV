class Solution:
    def decodeString(self, s: str) -> str:
        it = iter(s)
        return self.recursiveImplement(s, it)

    def recursiveImplement(self, s: str, it) -> Tuple:
        ret, times = [], 0
        for c in it:
            if c.isdigit():
                times = 10*times + int(c)
            elif c is '[':
                ret.append(times * self.recursiveImplement(s,it))
                times = 0
            elif c is ']':
                break
            else:
                ret.append(c)
        return "".join(ret)
        

s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "3[acb]"
s = "100[leetcode]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
#"zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
sol = Solution()
sol.decodeString(s)