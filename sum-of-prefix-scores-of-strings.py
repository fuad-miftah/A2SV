class TrieNode:
    def __init__(self,val):
        self.kids = {}
        self.val = val
        self.count = 0
        self.eow = False
class Solution:
    def __init__(self):
        self.root = TrieNode("*")
        self.root.eow = True

    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode(ch)
            node = node.kids[ch]
            node.count += 1
        node.eow = True

    def prefixCount(self,word):
        count = 0
        node = self.root
        for ch in word:
            node = node.kids[ch]
            count += node.count
        return count


    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        res = []
        for word in words:
            node = self.root
            res.append(self.prefixCount(word))
        return res