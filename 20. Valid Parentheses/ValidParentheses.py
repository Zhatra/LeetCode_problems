class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue    #stack[-1] es el ultimo valor agregado a la pila osea el top 
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
