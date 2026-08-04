class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        def closed(right):
            if (right == "}" and stack[-1] == "{") or \
               (right == ")" and stack[-1] == "(") or \
               (right == "]" and stack[-1] == "["):
               return True
            return False


        for char in s:
            if len(stack) == 0 and (char == "}" or \
                                    char == "]" or \
                                    char == ")"):
                return False

            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == "}" or char == "]" or char == ")":
                if not closed(char):
                    return False
                stack.pop()

        if len(stack) != 0:
            return False

        return True
        