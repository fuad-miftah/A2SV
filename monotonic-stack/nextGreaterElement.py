class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        for i in nums1:
            indexe = nums2.index(i) 
            if indexe == len(nums2) - 1:
                output.append(-1)
            else:
                indexe += 1
                while indexe < len(nums2):
                    if nums2[indexe] > i:
                        output.append(nums2[indexe])
                        break
                    if indexe == len(nums2) - 1:
                        output.append(-1)
                    indexe += 1
                
        return output



nums1 = [4,1,2]
nums2 = [1,3,4,2]
sol = Solution()
sol.nextGreaterElement(nums1,nums2)