class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        output = 0
        while right >= left:
            if people[right] + people[left] <= limit:
                right-=1
                left+=1
            else:
                right-=1
            output+=1
        return output
            