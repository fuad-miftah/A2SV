class Solution:
    def countingValleys(self , steps, path):
        count = level = 0
        d = {'U':1, 'D':-1}
        print(d)

        for p in path:
            level += d[p]
            
            if level == 0 and p == 'U':
                count += 1
        print(count)
        #return count


path = "UDDDUDUU"
#path = "UDDUUDUUDDD"
#path = "DDUUDDUDUUUD"
sol = Solution()
sol.countingValleys(12,path)