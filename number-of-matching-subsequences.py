class TrieNode:
    def __init__(self):
        self.kids = dict()

class Trie:
    def __init__(self, word):
        self.root = TrieNode()
        self.dic = defaultdict(list)
        size = len(word)
        for i in range(size):
            self.dic[word[i]].append(i)

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            node = node.kids[ch]

    def search(self, word):
        node = self.root
        indx = -1
        for ch in word:
            temp = bisect_left(self.dic[ch], indx)
            if temp == len(self.dic[ch]) or (indx > self.dic[ch][temp]):
                return False
            indx = self.dic[ch][temp] + 1
            node = node.kids[ch]
        return True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie(s)
        for word in words:
            trie.insert(word)

        res = 0
        for word in words:
            if trie.search(word):
                res += 1
        
        return res