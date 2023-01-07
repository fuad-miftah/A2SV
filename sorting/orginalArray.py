class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        orginalArr = []
        notDouble = False
        
        while notDouble == False
            #print(changed[0])
            print(len(changed))
            if changed[0] * 2 in changed:
                orginalArr.append(changed[0])
                changed.remove(changed[0]*2)
                changed.remove(changed[0])
                if len(changed) == 0:
                    notDouble = True
                print(len(changed))
            else:
                notDouble = True
            
        print(orginalArr)
        return(orginalArr)




changed = [1,3,4,2,8,6]
changed = [0,0]
sol = Solution()
sol.findOriginalArray(changed)