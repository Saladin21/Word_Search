class TrieNode:
    def __init__(self):
        self.children = {}
        #bernilai true jika node merupakan akhir dari kata
        self.isEndofWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.shortestWordLength = 0

    def insert(self, string):
        p = self.root
        n = len(string)
        if (n < self.shortestWordLength):
            self.shortestWordLength = n
        for i in range (n):
            c = string[i]
            if not (c in p.children.keys()):
                p.children[c] = TrieNode()
            p = p.children[c]
            if (i == n-1):
                p.isEndofWord = True

    def search(self, string):
        p = self.root
        check = True
        length = 0
        n = len(string)
        i = 0
        while (check and i < n and len(p.children) != 0):
            c = string[i]
            if (c in p.children.keys()):
                p = p.children[c]
                i+=1
                if p.isEndofWord:
                    length = i
                
            else:
                check = False
        return length
    
    def isRootChildren(self, char):
        return char in self.root.children.keys()

