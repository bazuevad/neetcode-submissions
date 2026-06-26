class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(","]": "[", "}":"{"}
        open_braces = set(["(", "[", "{"])
        if len(s)%2!=0:
            return False
        stack = []
        for i in s:
            if i in open_braces:
                stack.append(i)
            else:
                if stack:
                    next_brace = stack.pop()
                    if map.get(i)!=next_brace:
                        return False
                else:
                    return False
        return len(stack)==0