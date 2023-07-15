class TrieNode:
    def __init__(self):
        self.children = {} # note we not actually saving the word in node
        # we will be inserting it like this:
        # children["a"] = TrieNode()
        self.endOfWord = False # true if char is last

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                # hasnt been inserted yet
                curr.children[c] = TrieNode() # Again, this is how we insert
            curr = curr.children[c] # if its alr inserted we move to the next one
        # set curr to last character already then set to True
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False # doesnt exist return earlier
            # if it does
            curr = curr.children[c]
        return curr.endOfWord # if it sets to True it will return true

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True # u reach here means the rest are correct


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)