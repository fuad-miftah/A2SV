class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ressult = []
        for i in range(len(l)):
            subArr = nums[l[i]:r[i]+1]
            subArr.sort()
            dif = subArr[1] - subArr[0]
            
            for j in range(len(subArr)-1):
                arthimetic = True
                if subArr[j+1] - subArr[j] == dif:
                    continue
                else:
                    arthimetic = False
                    break
            ressult.append(arthimetic)

        #print(ressult)
        return ressult