class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        travel = [i-j for i,j in zip(gas,cost)]
        
        n = len(gas)
        cur_sum = 0
        idx = -1

        for i in range(2*n):
            i = i%n
            if cur_sum + travel[i] < 0:
                cur_sum = 0
                idx = -1
            
            else:
                cur_sum += travel[i]
                if idx == i:
                    return idx

                if idx == -1:
                    idx = i 
        
        return -1