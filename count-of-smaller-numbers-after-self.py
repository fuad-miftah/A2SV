class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        enum = list(enumerate(nums))
        self.divide(enum,res)
        return res

    def divide(self,enum,res):
        if len(enum) <= 1:
            return enum
        mid = len(enum) // 2

        l = self.divide(enum[ : mid],res)
        r = self.divide(enum[mid : ],res)

        return self.merge(l,r,res)
    
    def merge(self,l,r,res):

        inversion_count = 0
    
        mergedArr = []
        p1 = 0
        p2 = 0

        while p1 < len(l) and p2 < len(r):
            if l[p1][1] <= r[p2][1]:
                mergedArr.append(l[p1])
                res[l[p1][0]] += inversion_count 
                p1+=1
            else:
                mergedArr.append(r[p2])
                inversion_count += 1
                p2+=1

        while p1 < len(l):
            mergedArr.append(l[p1])
            res[l[p1][0]] += inversion_count
            p1+=1
        while p2 < len(r):
            mergedArr.append(r[p2])
            p2+=1

        return mergedArr