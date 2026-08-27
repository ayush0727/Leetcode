class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();
    vector<int> freq(26, 0);
    for (char c : s) freq[c - 'a']++;
    string result;
    function<bool(int)> dfs = [&](int idx) {
        if (idx == n) return result > target;
        for (int c = 0; c < 26; c++) {
            if (freq[c] == 0) continue;
            char ch = 'a' + c;
            result.push_back(ch);
            freq[c]--;
            if (result[idx] > target[idx]) {
                string temp = result;
                for (int k = 0; k < 26; k++)
                    temp.append(freq[k], 'a' + k);
                if (temp > target) {
                    result = temp;
                    return true;
                }
            } else if (result[idx] == target[idx]) {
                if (dfs(idx + 1)) return true;
            }
            freq[c]++;
            result.pop_back();
        }
        return false;
    };

    result.clear();
    if (dfs(0)) return result;
    return "" ;   
    }
};