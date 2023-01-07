class Solution:
    def dailyTempratures(self , tempratures):
        output = []
        for i in range(len(tempratures)):
            counter = -1
            for j in range(i+1, len(tempratures)):
                
                if tempratures[i] < tempratures[j]:
                    counter += 1
                    output.append(counter + 1)
                    break
                elif j == len(tempratures) - 1:
                    output.append(0)
                    break
                counter += 1
        output.append(0)
        print(output)
            


tempratures = [73,74,75,71,69,72,76,73]
tempratures = [30,40,50,60]
tempratures = [30,90,60]
sol = Solution()
sol.dailyTempratures(tempratures)