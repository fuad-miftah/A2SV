class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        queue = []
        for i in range(1, n+1):
            queue.append(i)
        k = k-1
        
        def helper(queue, k, curr):
            if len(queue) == 1:
                return queue[0]

            j = 0
            while j < k:
                if curr + 1 >= len(queue):
                    curr = 0
                    j+=1
                else:
                    curr+=1
                    j+=1
            queue.pop(curr)
       
            if curr == len(queue):
                curr = 0
            helper(queue, k, curr)
            return queue[0]
        
        res = helper(queue,k , 0)
        
        return res
        

       

sol = Solution()
sol.findTheWinner(6,5)