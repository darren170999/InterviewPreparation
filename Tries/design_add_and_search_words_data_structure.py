class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self._search_helper(word, self.root)

    def _search_helper(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node.endOfWord

        if word[0] != ".":
            if word[0] not in node.children:
                return False
            return self._search_helper(word[1:], node.children[word[0]])
        else:
            for child in node.children.values():
                if self._search_helper(word[1:], child):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)