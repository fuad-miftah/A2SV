class Solution(object):
    def sortSentence(self, s):
        splitedArr = s.split()
        newArr = ['','','','','','','','','']
        newString = ""
        for i in range(len(splitedArr)):
            if splitedArr[i].endswith('1'):
                newArr[0] = splitedArr[i].replace('1', ' ')
            elif splitedArr[i].endswith('2'):
                newArr[1] = splitedArr[i].replace('2', ' ')
            elif splitedArr[i].endswith('3'):
                newArr[2] = splitedArr[i].replace('3', ' ')
            elif splitedArr[i].endswith('4'):
                newArr[3] = splitedArr[i].replace('4', ' ')
            elif splitedArr[i].endswith('5'):
                newArr[4] = splitedArr[i].replace('5', ' ')
            elif splitedArr[i].endswith('6'):
                newArr[5] = splitedArr[i].replace('6', ' ')
            elif splitedArr[i].endswith('7'):
                newArr[6] = splitedArr[i].replace('7', ' ')
            elif splitedArr[i].endswith('8'):
                newArr[7] = splitedArr[i].replace('8', ' ')
            else:
                newArr[8] = splitedArr[i].replace('9', ' ')

        for i in range(9):
            newString = newString + newArr[i]
        
        return newString.rstrip(" ")    
            


sol = Solution()
sol.sortSentence("Myself2 Me1 I4 and3")