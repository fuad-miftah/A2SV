class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0]*1001
        for t in trips:
            numPass,start,end = t
            changes[start]+=numPass
            changes[end]-=numPass
        currPass = 0
        for change in changes:
            currPass+=change
            if currPass > capacity:
                return False
        return True