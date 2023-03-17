class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1]*len(nums1)
        dic = {}
        for i in range(len(nums1)):
            dic[nums1[i]] = i
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                indx = stack.pop()
                if nums2[indx] in dic:
                    output[dic[nums2[indx]]] = nums2[i]
            stack.append(i)
        
        return output