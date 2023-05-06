class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        arr = [(-count, word) for word, count in counts.items()]
        heapify(arr) 
        return [heappop(arr)[1] for _ in range(k)]