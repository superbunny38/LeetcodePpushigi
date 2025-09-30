class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        matching = {'(':')', '{':'}','[':']'}
        for bracket in s:
            if bracket in matching:
                stack.append(bracket)
            elif len(stack) == 0 or matching[stack.pop()] != bracket:
                return False
        return len(stack) == 0