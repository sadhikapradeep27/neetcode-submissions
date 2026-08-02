class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        maps={")":"(","}":"{","]":"["}
        for  ch in s:
            if ch not in maps:
                stack.append(ch)
            else:
                if not stack or stack[-1]!=maps[ch]:
                    return False
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False