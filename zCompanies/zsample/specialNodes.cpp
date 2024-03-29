void dfs(int x, int p, const vector<vector<int>> &con, int d, int &maxd, vector<int> &nodes) {
    if (d > maxd) {
        maxd = d;
        nodes.clear();
    }
    if (d == maxd) {
        nodes.push_back(x);
    }
    for (int y : con[x]) {
        if (y != p) {
            dfs(y, x, con, d + 1, maxd, nodes);
        }
    }
}

vector<int> solution(int n, const vector<int> &tree_from, const vector<int> &tree_to) {
    vector<vector<int>> e(n);
    for (int i = 0; i < tree_from.size(); ++i) {
        e[tree_from[i] - 1].push_back(tree_to[i] - 1);
        e[tree_to[i] - 1].push_back(tree_from[i] - 1);
    }
    vector<unordered_set<int>> con(n);
    for (int i = 0; i < n; ++i) {
        con[i] = unordered_set<int>(e[i].begin(), e[i].end());
    }
    
    unordered_set<int> nodes;
    queue<int> q;
    for (int i = 0; i < n; ++i) {
        nodes.insert(i);
        if (con[i].size() == 1) {
            q.push(i);
        }
    }
    while (!q.empty() && nodes.size() > 2) {
        for (int i = q.size(); i; --i) {
            const int x = q.front(), y = *con[x].begin();
            q.pop();
            nodes.erase(x);
            con[y].erase(x);
            if (con[y].size() == 1) {
                q.push(y);
            }
        }
    }
    vector<int> ind1, ind2;
    int m = 0;
    if (nodes.size() == 1) {
        dfs(*nodes.begin(), -1, e, 0, m = 0, ind1);
    } else {
        auto t2 = nodes.begin(), t1 = t2++;
        dfs(*t1, *t2, e, 0, m = 0, ind1);
        dfs(*t2, *t1, e, 0, m = 0, ind2);
    }
    vector<int> r(n);
    for (int i : ind1) {
        r[i] = 1;
    }
    for (int i : ind2) {
        r[i] = 1;
    }
    return r;
}

void print(const vector<int> &v) {
    for (int x : v) {
        printf("%d ", x);
    }
    puts("");
}
int main() {
    print(solution(1, {}, {}));
    print(solution(2, {2}, {1}));
    print(solution(3, {2, 1}, {1, 3}));
    print(solution(7, {1, 2, 3, 3, 1, 1}, {2, 3, 4, 5, 6, 7}));
    return 0;
}