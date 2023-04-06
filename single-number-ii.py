class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [0] * 32
        negative = 0
        for num in nums:
            indx = 0
            if num > 0:
                while num > 0:
                    if num & 1:
                        res[indx] += 1
                    num >>= 1
                    indx += 1
            else:
                negative += 1
                num = abs(num)
                while num > 0:
                    if num & 1:
                        res[indx] += 1
                    num >>= 1
                    indx += 1
        ans = [0] * 32
        for i in range(len(res)):
            if res[i] % 3 != 0:
                ans[i] = 1

        while ans[-1] == 0:
            ans.pop()
        ans.reverse()

        res = "".join( str(e) for e in ans )
        
        if negative % 3 == 0:
            return int(res , 2)
        else:
            return -(int(res , 2))