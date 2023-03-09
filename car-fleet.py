class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        n=len(cars)
        stack = []
        for i in range(n-1,-1,-1):
            p,s = cars[i]
            arrive = (target-p)/s
            if not stack or arrive>stack[-1]:
                stack.append(arrive)
        return len(stack)