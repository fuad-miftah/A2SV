class Solution(object):
    def merge(self, intervals)
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        intervals.sort()
        #for i in range(len(intervals)):

        for i in intervals:
            k = 0

            x = i[0]
            y = i[1]
            
            for j in range(k,len(intervals)):
                
                if y >= intervals[j][0] and y <= intervals[j][1]:
                    print("entered 1")
                    y = intervals[j][1]
                elif y >= intervals[j][0] and y >= intervals[j][1]:
                    print("2")
                    continue
                elif y <= intervals[j][0]:
                    y = intervals[j][0]
                else:
                    if j != i+1:
                        print("3")
                        result.append([x,y])
                        k+=1
                        break
                    else:
                        result.append([x,y])
                        k+=1
                        break
                 

        return result