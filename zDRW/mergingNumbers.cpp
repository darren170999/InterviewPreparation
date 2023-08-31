#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int>& nums) {
    vector<vector<int>> dp = {{0, 0}, {0, nums[0]}};
    
    for (size_t i = 1; i < nums.size(); ++i) {
        int dp0 = max(dp[dp.size() - 2][0], dp[dp.size() - 2][1]) + stoi(to_string(nums[i - 1]) + to_string(nums[i]));
        int dp1 = max(dp[dp.size() - 1][0], dp[dp.size() - 1][1]) + nums[i];
        
        dp.push_back({dp[dp.size() - 1][1], max(dp0, dp1)});
    }
    
    return max(dp[dp.size() - 1][0], dp[dp.size() - 1][1]);
}

int main() {
    vector<int> nums1 = {2, 3, 15};
    vector<int> nums2 = {2, 2, 3, 5, 4, 0};
    vector<int> nums3 = {3, 19, 191, 91, 3};
    vector<int> nums4 = {12, 6, 18, 10, 1, 0};
    vector<int> nums5 = {2, 1, 0, 1, 2, 9, 1, 0};

    cout << solve(nums1) << endl;  // Output: 23
    cout << solve(nums2) << endl;  // Output: 270
    cout << solve(nums3) << endl;  // Output: 361
    cout << solve(nums4) << endl;  // Output: 402
    cout << solve(nums5) << endl;  // Output: 1120
    
    return 0;
}
