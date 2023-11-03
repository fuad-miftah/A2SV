class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
            
        dates.sort()

        popul = max_popul = max_year = 0
        for year, diff in dates:
            popul += diff
            if popul > max_popul:
                max_popul = popul
                max_year = year
        
        return max_year