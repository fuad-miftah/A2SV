class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest = ""
        stri = []
        for i in nums:
            stri.append(str(i))


        for i in range(len(stri)):
            for j in range(i+1,len(stri)):
                if stri[i] + stri[j] < stri[j] + stri[i]:
                    stri[i],stri[j] = stri[j], stri[i]

        allTrue = False
        for i in stri:
            if i == "0":
                allTrue = True
            else:
                allTrue = False
                break
        if allTrue == False:
            for i in stri:
                largest += i
        else:
            largest = "0"

        return largest