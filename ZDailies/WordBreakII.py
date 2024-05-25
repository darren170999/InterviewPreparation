class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # build Trie
        newTrie = Trie()
        # Add words to Trie
        for word in wordDict:
            newTrie.insert(word)
        # Store ans in a dp set
        dp = {len(s): [""]}
        # Iterate to find valid sentences bottom up
        def sentences(ind):
            if ind in dp:
                return dp[ind]
            # Init current node to root of trie + valid
            curr = newTrie.root
            valid_sentences = []
            # From this position onwards are there any matching things in trie
            for j in range(ind, len(s)):
                # Yes ...
                if s[j] not in curr.children:
                    break
                # If reach here, go to children, since still valid
                curr = curr.children[s[j]]
                if curr.isEnd:
                    wordToAdd = s[ind:j+1]
                    for parts in sentences(j+1):
                        valid_sentences.append(f"{wordToAdd} {parts}".strip())
            dp[ind] = valid_sentences
            return valid_sentences
        return sentences(0)
