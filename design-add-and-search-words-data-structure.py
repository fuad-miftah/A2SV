class TrieNode:
    def __init__(self):
        self.kids = {}
        self.eow = 0
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            node = node.kids[ch]
        node.eow = 1
        

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): 
                return node.eow
               
            if word[i] == ".":
                for child in node.kids:
                    if dfs(node.kids[child], i+1): 
                        return True
                    
            if word[i] in node.kids:
                return dfs(node.kids[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)