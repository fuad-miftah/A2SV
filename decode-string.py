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