def is_integer(s):
    try:
        int(s)  # Try converting the string to an integer
        return True
    except ValueError:
        return False
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if is_integer(token):
                print(f"number {token} appended!")
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                print(f"{n1} {token} {n2}")
                if token == '+':
                    stack.append(int(n1+n2))
                elif token == '-':
                    stack.append(int(n2-n1))
                elif token == '*':
                    stack.append(int(n2*n1))
                else:
                    stack.append(int(n2/n1))
        return stack[-1]
    
# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = Solution().evalRPN(tokens=tokens)
print(s)