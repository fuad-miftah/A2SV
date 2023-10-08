class TrieNode:
    def __init__(self):
        self.kids = {}
        self.indx = -1

class WordFilter(object):
    def __init__(self, words):
        self.root = TrieNode()
        
        for indx, word in enumerate(words):
            self.addWord(indx, word)
    
    def addWord(self, indx, word):
        for i in range(len(word)-1, -2, -1):
            newStr = word[i+1:] + '#' + word
            node = self.root
            node.indx = indx
            
            for ch in newStr:
                if ch not in node.kids:
                    node.kids[ch] = TrieNode()
                node = node.kids[ch]
                node.indx = indx
        

    def f(self, prefix, suffix):
        node = self.root
        newStr = suffix + '#' + prefix
        
        for ch in newStr:
            if ch not in node.kids:
                return -1
            node = node.kids[ch]
        
        return node.indx