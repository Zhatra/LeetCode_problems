#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
    int maxReach = 0;
    for (int i = 0; i < nums.size(); ++i) {
        // If current position is beyond the farthest reachable position, return false
        if (i > maxReach) return false;
        // Update the farthest reachable position
        maxReach = max(maxReach, i + nums[i]);
        // If farthest reachable position is beyond or at the last index, return true
        if (maxReach >= nums.size() - 1) return true;
    }
    return false;
}
};