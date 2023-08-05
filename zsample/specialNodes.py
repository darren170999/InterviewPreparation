from collections import defaultdict
def solve(n, tree_from, tree_to):
    G = defaultdict(list)
    for v,w in zip(tree_from, tree_to):
        G[v].append(w)
        G[w].append(v)
    maxlevel = -1
    def dfs(v, level, prev, ends):
        nonlocal maxlevel
        if level > maxlevel:
            maxlevel = level
            ends.clear()
            ends.add(v)
        elif level == maxlevel:
            ends.add(v)
        for w in G[v]:
            if w == prev: continue
            dfs(w,level+1,v,ends)
    ends1 = set()
    dfs(1, 0, -1, ends1)
    ends2 = set()
    dfs(next(iter(ends1)), 0, -1, ends2)
    return list(ends1 | ends2)
print(solve(7, [1,2,3,3,1,1], [2,3,4,5,6,7]))