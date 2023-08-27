# 
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        
        while queue:
            currWord, level = queue.popleft()
            
            if currWord == endWord:
                return level
            
            for i in range(len(currWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = currWord[:i] + c + currWord[i+1:]
                    
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)  # Avoid revisiting the same word
                        queue.append((nextWord, level + 1))
        
        return 0

class Solution:
    from collections import deque
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == None or endWord == None:
            return 0
        if endWord not in wordList:
            return 0
        n = len(wordList[0])
        visit = set()
        queue = deque()
        queue.append((beginWord, 1)) # Simuiltaneous BFS
        visit.add(beginWord)
        def check(w1,w2):
            n = len(w1)
            tolerance = 1
            for i in range(n):
                if w1[i] != w2[i]:
                    tolerance -= 1
                if tolerance < 0:
                    return False
            return True
        while queue:
            # print(queue)
            curr, level = queue.popleft()
            if curr == endWord:
                return level
            if wordList:
                for word in wordList:
                    # print(check(curr,word))
                    if check(word, curr) and word not in visit:
                        visit.add(word)
                        queue.append((word, level+1))
        return 0