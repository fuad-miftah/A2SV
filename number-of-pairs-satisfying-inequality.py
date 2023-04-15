class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        difArr = []
        self.diff = diff
        self.res = 0
        for i in range(len(nums1)):
            difArr.append(nums1[i]-nums2[i])

        def divide(difArr):
            if len(difArr) == 1:
                return difArr

            mid = len(difArr) // 2
            
            l = divide(difArr[ : mid])
            r = divide(difArr[mid: ])
        
            return merge(l,r)
        
        def merge(l,r):
            j = 0
            for i in range(len(l)):
                while j < len(r):
                    if l[i] - self.diff <= r[j]:
                        break
                    j+=1
                self.res += len(r) - j
            
            mergedArr = []
            p1 = 0
            p2 = 0
            while p1 < len(l) and p2 < len(r):
                if l[p1] < r[p2]:
                    mergedArr.append(l[p1])
                    p1+=1
                else:
                    mergedArr.append(r[p2])
                    p2+=1

            while p1 < len(l):
                mergedArr.append(l[p1])
                p1+=1
            while p2 < len(r):
                mergedArr.append(r[p2])
                p2+=1

            return mergedArr
            
        divide(difArr)
        
        return self.res