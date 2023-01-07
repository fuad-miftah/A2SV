class Solution:
    def nextGreaterElement(self , nums1, nums2):
        output=[]
        for i in nums1:
            foundAt = nums2.index(i)
            if foundAt == len(nums2) - 1:
                output.append(-1)
            else:
                if nums2[foundAt + 1] > i:
                    output.append(nums2[foundAt + 1])
                else:
                    output.append(-1)
        print(output)



nums1 = [4,1,2]
nums2 = [1,3,4,2]
sol = Solution()
sol.nextGreaterElement(nums1,nums2)