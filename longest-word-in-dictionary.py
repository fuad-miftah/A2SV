class TrieNode:
    def __init__(self,val):
        self.kids = {}
        self.val = val
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
        node.eow = True

    def dfs(self,node):
        if node and node.eow == True and len(node.kids) == 0:
            return node.val
        if node and node.eow == False:
            return ""
        res = ""
        for child in node.kids:
            r = self.dfs(node.kids[child])
            if len(r) > len(res):
                res = r
            elif len(r) == len(res) and res > r:
                res = r
        return node.val + res

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
        node = self.root
        res = self.dfs(node)
        return res[1:]