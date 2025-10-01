class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in p.keys():
                if not stack:
                    return False
                popped = stack.pop()
                if popped != p[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
