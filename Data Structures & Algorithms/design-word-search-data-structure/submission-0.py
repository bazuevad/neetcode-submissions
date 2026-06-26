
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            n = ord(i) - ord('a')
            if curr.children[n]==None:
                curr.children[n] = Trie()
            curr = curr.children[n]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(start, root):
            if root is None:
                return False
            curr = root

            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    for kid in curr.children:
                        if kid is not None:
                            if dfs(i+1,kid):
                                return True
                    return False
                else:
                    n = ord(c) - ord('a')
                    if curr.children[n] is None:
                        return False
                    curr = curr.children[n]
            return curr.word
        return dfs(0,self.root)

