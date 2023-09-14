class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        vector<string> ans;
        unordered_map<string, vector<string>> adj; // Use unordered_map with string keys
        sort(tickets.begin(), tickets.end());

        for (const vector<string>& ticket : tickets) {
            string from = ticket[0];
            string to = ticket[1];
            adj[from].push_back(to);
        }

        dfs("JFK", ans, adj, tickets);
        return ans;
    }

    bool dfs(const string& source, vector<string>& ans, unordered_map<string, vector<string>>& adj, vector<vector<string>>& tickets) {
        ans.push_back(source);

        if (ans.size() == tickets.size() + 1) {
            return true;
        }

        if (adj.find(source) == adj.end()) {
            ans.pop_back();
            return false;
        }

        vector<string> temp = adj[source];

        for (size_t i = 0; i < temp.size(); ++i) {
            string v = temp[i];
            adj[source].erase(adj[source].begin() + i);
            if (dfs(v, ans, adj, tickets)) {
                return true;
            }
            adj[source].insert(adj[source].begin() + i, v);
        }

        ans.pop_back();
        return false;
    }
};
