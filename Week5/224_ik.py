class Solution:
    def calculate(self, s: str) -> int:
        ADD = lambda x, y: x + y
        SUB = lambda x, y: x - y
        stack = []
        num = 0
        result = 0
        op = ADD

        for c in s:
            if c == " ":
                continue
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result = op(result, num)
                num = 0
                op = ADD if c == "+" else SUB
            elif c == "(":
                stack.append((result, op)) # Save context
                result = 0
                op = ADD
            elif c == ")":
                result = op(result, num)
                res, oop = stack.pop()
                result = oop(res, result)
                num = 0
        result = op(result, num)
        return result