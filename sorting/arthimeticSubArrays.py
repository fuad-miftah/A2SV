class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        subArr = []
        outputArr = []
        for i in range(len(l)):
            left = l[i]
            right = r[i] + 1
            subArr.append(nums[left:right])
        #print(subArr)
        for i in range(len(subArr)):
            for j in range(len(subArr[i])):
                for k in range(len(subArr[i])-1):
                    if subArr[i][k] > subArr[i][k+1]:
                        subArr[i][k], subArr[i][k+1] = subArr[i][k+1], subArr[i][k]
            #print(subArr)
            dif = 0
            for m in range(len(subArr[i])-1):
                
                if m == 0:
                    dif = subArr[i][m] - subArr[i][m+1]
                    if len(subArr[i]) == 2:
                        outputArr.append(True)
                        break
                else:
            
                    if dif != subArr[i][m] - subArr[i][m+1]:
                        print(i)
                        outputArr.append(False)
                        break
                    elif m == len(subArr[i])-2:
                        print(i)
                        outputArr.append(True)
                        break
        return outputArr 








nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r=[4,4,9,7,9,10]
sol = Solution()
sol.checkArthimeticSubarrays(nums , l , r)