class TrieNode:
    def __init__(self):
        self.kids = [None] * 26
        self.val = 0
        self.eow = -1
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if node.kids[ord(ch) - ord("a")] == None:
                trie = TrieNode()
                node.kids[ord(ch)-ord("a")] = trie
            
            node = node.kids[ord(ch)-ord("a")]
            node.val += val
        if node.eow != -1:
            self.override(node.eow, key)
        node.eow = val


    def override(self,val,key):
        node = self.root
        for ch in key:
            node = node.kids[ord(ch)-ord("a")]
            node.val -= val
   
                
    def sum(self, prefix: str) -> int:
        node = self.root

        res = 0
        for ch in prefix:
            if node.kids[ord(ch) - ord("a")] == None:
                return 0
            node = node.kids[ord(ch)-ord("a")]
          
        return node.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)