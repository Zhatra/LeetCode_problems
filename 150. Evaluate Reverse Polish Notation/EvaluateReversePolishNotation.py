class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Use a list as a stack

        for token in tokens:
            if token in ("+", "-", "*", "/"):
                # If the token is an operator, pop the last two elements from the stack
                b = stack.pop()
                a = stack.pop()

                # Perform the operation and push the result back to the stack
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # In Python, dividing two integers truncates towards zero by default
                    stack.append(int(a / b))
            else:
                # If the token is a number, push it onto the stack
                stack.append(int(token))

        # After processing all tokens, the final result will be the only element left on the stack
        return stack[0]