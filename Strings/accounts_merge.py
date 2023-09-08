class UnionFind:
    def __init__(self,n): # Constructor pass in length of nodes
        self.par = [i for i in range(n)] # each node is parent of itself
        self.rank = [1] * n # rank is size of each disjoint sets
    def find(self, x): # Constant time
        while x!= self.par[x]:
            self.par[x] = self.par[self.par[x]] # path compression
            x = self.par[x]
        return x
    def union(self, x1, x2): # Constant time
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
class Solution:
    def accountMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # map email -> index of acc
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(1, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list) # index of acc -> list of emails

        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res