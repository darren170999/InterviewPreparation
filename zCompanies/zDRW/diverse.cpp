#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::string solution(int A, int B, int C) {
        std::vector<std::pair<char, int>> counts = {{'a', A}, {'b', B}, {'c', C}};
        std::string result;

        while (!counts.empty()) {
            std::sort(counts.begin(), counts.end(), [](const std::pair<char, int>& a, const std::pair<char, int>& b) {
                return a.second > b.second;
            });

            if (!result.empty() && result.back() == counts[0].first) {
                if (counts[1].second > 0) {
                    result.push_back(counts[1].first);
                    --counts[1].second;
                } else if (counts[2].second > 0) {
                    result.push_back(counts[2].first);
                    --counts[2].second;
                } else {
                    break; // No more characters to add
                }
            } else {
                result.push_back(counts[0].first);
                --counts[0].second;
            }

            counts.erase(std::remove_if(counts.begin(), counts.end(), [](const std::pair<char, int>& c) {
                return c.second == 0;
            }), counts.end());
        }

        return result;
    }
};

int main() {
    Solution solution;

    std::cout << solution.solution(3, 1, 0) << std::endl;  // Output: "aaba"
    std::cout << solution.solution(1, 4, 4) << std::endl;  // Output: "abbcbcbcc"
    std::cout << solution.solution(1, 3, 0) << std::endl;  // Output: "babb"

    return 0;
}
