import collections
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        # orginalArr = []
        # notDouble = False
        
        # while notDouble == False
        #     #print(changed[0])
        #     print(len(changed))
        #     if changed[0] * 2 in changed:
        #         orginalArr.append(changed[0])
        #         changed.remove(changed[0]*2)
        #         changed.remove(changed[0])
        #         if len(changed) == 0:
        #             notDouble = True
        #         print(len(changed))
        #     else:
        #         notDouble = True
            
        # print(orginalArr)
        # return(orginalArr)
        n = len(changed)
        if n%2 :
            return []
        count = collections.Counter(changed)
        changed.sort()
        ans = []

        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                ans.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                ans.append(num)
        

        if len(ans) == n//2:
            return ans
        else:
            return []





changed = [1,3,4,2,8,6]
#changed = [0,0]
sol = Solution()
print(sol.findOriginalArray(changed))