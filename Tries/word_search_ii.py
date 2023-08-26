class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # have to use Trie(Prefix Tree) in order to solve optimally
        root = TrieNode()
        for word in words:
            root.addWord(word)
        ans = set()
        m, n = len(board), len(board[0])
        path = set()
        def dfs(r, c, node, word):
            if(r<0 or c<0 or r>=m or c>=n or board[r][c] not in node.children or (r,c) in path): # if out of bounds or if visited befgore or if curr word is not right
                return False
            path.add((r,c)) # currently visited this path for this call
            # process current node
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord: # found word
                ans.add(word)
            # call dfs on the other four adj nodes
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            path.remove((r,c))
        for r in range(m):
            for c in range(n):
                dfs(r,c,root,"")
        return list(ans)