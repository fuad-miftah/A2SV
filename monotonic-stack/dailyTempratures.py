class Solution:
    def dailyTempratures(self , tempratures):
        output = [0] * len(tempratures)
        stack = []
        for today_day, today_temp in enumerate(tempratures):
            
            while stack and today_temp > stack[-1][0]:
                past_day, past_ind = stack.pop()
                output[past_ind] = (today_day - past_ind)
            stack.append([today_temp, today_day])

        print(output)
        return(output)
            


tempratures = [73,74,75,71,69,72,76,73]
#tempratures = [30,40,50,60]
#tempratures = [30,90,60]
sol = Solution()
sol.dailyTempratures(tempratures)