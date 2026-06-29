class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        code = [0] * 26
        for ch in s:
            code[ord(ch)-ord('a')]+=1
        for ch in t:
            code[ord(ch)-ord('a')]-=1
        return all(i == 0 for i in code)