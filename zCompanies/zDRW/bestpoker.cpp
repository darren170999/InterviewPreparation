// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int solve(vector<int>& nums) {
//     vector<vector<int>> dp = {{0, 0}, {0, nums[0]}};
    
//     for (size_t i = 1; i < nums.size(); ++i) {
//         int dp0 = max(dp[dp.size() - 2][0], dp[dp.size() - 2][1]) + stoi(to_string(nums[i - 1]) + to_string(nums[i]));
//         int dp1 = max(dp[dp.size() - 1][0], dp[dp.size() - 1][1]) + nums[i];
        
//         dp.push_back({dp[dp.size() - 1][1], max(dp0, dp1)});
//     }
    
//     return max(dp[dp.size() - 1][0], dp[dp.size() - 1][1]);
// }

// int main() {
//     vector<int> nums1 = {2, 3, 15};
//     vector<int> nums2 = {2, 2, 3, 5, 4, 0};
//     vector<int> nums3 = {3, 19, 191, 91, 3};
//     vector<int> nums4 = {12, 6, 18, 10, 1, 0};
//     vector<int> nums5 = {2, 1, 0, 1, 2, 9, 1, 0};

//     cout << solve(nums1) << endl;  // Output: 23
//     cout << solve(nums2) << endl;  // Output: 270
//     cout << solve(nums3) << endl;  // Output: 361
//     cout << solve(nums4) << endl;  // Output: 402
//     cout << solve(nums5) << endl;  // Output: 1120
    
//     return 0;
// }
#include <iostream>
#include <vector>
#include <algorithm>

int rankToValue(char rank) {
    if (isdigit(rank)) {
        return rank - '0';
    } else {
        switch (rank) {
            case 'A':
                return 14;
            case 'K':
                return 13;
            case 'Q':
                return 12;
            case 'J':
                return 11;
        }
    }
    return 0; // Invalid rank
}

std::string findBestHand(std::vector<std::string>& cards) {
    std::vector<char> ranks;
    std::vector<char> suits;

    for (const std::string& card : cards) {
        ranks.push_back(card[0]);
        suits.push_back(card[1]);
    }

    // Check for full house
    for (char rank : ranks) {
        int rankCount = std::count(ranks.begin(), ranks.end(), rank);
        if (rankCount >= 3) {
            std::vector<char> otherRanks;
            for (char otherRank : ranks) {
                if (otherRank != rank) {
                    otherRanks.push_back(otherRank);
                }
            }
            for (char otherRank : otherRanks) {
                int otherRankCount = std::count(otherRanks.begin(), otherRanks.end(), otherRank);
                if (otherRankCount >= 2) {
                    return "Full House";
                }
            }
        }
    }

    // Check for flush
    for (char suit : suits) {
        int suitCount = std::count(suits.begin(), suits.end(), suit);
        if (suitCount >= 5) {
            return "Flush";
        }
    }

    // Check for straight
    std::vector<int> numericRanks;
    for (char rank : ranks) {
        numericRanks.push_back(rankToValue(rank));
    }
    std::sort(numericRanks.begin(), numericRanks.end());
    for (size_t i = 0; i < numericRanks.size() - 4; ++i) {
        if (numericRanks[i] + 4 == numericRanks[i + 4]) {
            return "Straight";
        }
    }

    // Check for triple
    for (char rank : ranks) {
        int rankCount = std::count(ranks.begin(), ranks.end(), rank);
        if (rankCount >= 3) {
            return "Triple";
        }
    }

    // Check for pair
    for (char rank : ranks) {
        int rankCount = std::count(ranks.begin(), ranks.end(), rank);
        if (rankCount >= 2) {
            return "Pair";
        }
    }

    return "High Card";
}

int main() {
    std::vector<std::string> cards = {"10S", "AC", "AH", "10C", "10D", "5S", "6H"};
    std::string bestHand = findBestHand(cards);
    std::cout << "Best hand: " << bestHand << std::endl;

    return 0;
}