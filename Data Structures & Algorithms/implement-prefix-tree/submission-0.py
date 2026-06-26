class Trie:
    def __init__(self):
        self.children = [None]*26
        self.word = False
class PrefixTree:

    def __init__(self):
        self.head = Trie()

    def insert(self, word: str) -> None:
        curr = self.head
        for i in word:
            n = ord(i) - ord('a')
            if curr.children[n] == None:
                curr.children[n] = Trie()
            curr = curr.children[n]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.head
        for i in word:
            n = ord(i) - ord('a')
            if curr.children[n] == None:
                return False
            curr = curr.children[n]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for i in prefix:
            n = ord(i) - ord('a')
            if curr.children[n] == None:
                return False
            curr = curr.children[n]
        return True
        