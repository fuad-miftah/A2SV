class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        visited = set()
        for key in count:
            if count[key] in visited:
                return False
            visited.add(count[key])
        return True
        