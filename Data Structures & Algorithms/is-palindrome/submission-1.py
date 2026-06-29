class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        lo,hi = 0, len(s)-1
        while lo<=hi:
            if s[lo]!=s[hi]:
                return False
            lo+=1
            hi-=1
        return True