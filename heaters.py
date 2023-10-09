class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ind = 0 
        result = 0
        houses.sort()
        heaters.sort()
        for i in range(len(houses)):
            while ind < len(heaters) - 1 and abs(houses[i] - heaters[ind]) >= abs(houses[i] - heaters[ind +  1]):
                ind += 1
            result = max(result,abs(houses[i] - heaters[ind]))
            
        return result