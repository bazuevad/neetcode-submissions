from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastrep = 0
        last_seen = defaultdict(int)
        mx = 0
        for i,ch in enumerate(s):
            if ch in last_seen:
                lastrep = max(lastrep,last_seen[ch]+1)
            mx = max(mx,i-lastrep+1)
            last_seen[ch] = i
        return mx