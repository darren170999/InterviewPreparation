class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for t in path.split('/'):
            if t == '..':
                if result:
                    result.pop()
            elif t not in ('', '.'):
                result.append(t)
        
        return "/" + "/".join(result)