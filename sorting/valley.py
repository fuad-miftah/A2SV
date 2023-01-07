class Solution:
    def countingValleys(self , steps, path)
        count = 0
        step = 0
        current = ''
        for i in path:
            if i == 'D':
                if step > 0 or step < 0:
                    step -= 1
                    current = 'D'
                    #current = 'D'
                elif step == 0:
                    step -=1
                    current = 'D'
                    count += 1
                else:

                    if current == 'D' or current == '':
                        count += 1
                        step -= 1
                        current = 'D'
                    else:
                        step -= 1
                        current = 'D'

            elif i == 'U':
                step += 1
                current = 'U'
        print(count)


path = "UDDDUDUU"
path = "UDDUUDUUDDD"
path = "DDUUDDUDUUUD"
sol = Solution()
sol.countingValleys(12,path)