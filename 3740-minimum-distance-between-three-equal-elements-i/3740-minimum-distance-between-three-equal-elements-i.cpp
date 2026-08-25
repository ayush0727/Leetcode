class Solution {
public:
    int minimumDistance(vector<int>& nums) {
      unordered_map<int, vector<int>> positions;
    int n = nums.size();

    for (int i = 0; i < n; i++) {
        positions[nums[i]].push_back(i);
    }
    
    int ans = INT_MAX;
    for (auto &p : positions) {
        auto &idx = p.second;
        if (idx.size() >= 3) {
            sort(idx.begin(), idx.end());
            for (int i = 0; i + 2 < idx.size(); i++) {
                int dist = 2 * (idx[i+2] - idx[i]);
                ans = min(ans, dist);
            }
        }
    }
    
    return ans == INT_MAX ? -1 : ans;   
    }
};