class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []    
        
        for token in tokens:

            if token == "+":
                num2 = numStack.pop()
                num1 = numStack.pop()
                numStack.append(num1 + num2)
            elif token == "-":
                num2 = numStack.pop()
                num1 = numStack.pop()
                numStack.append(num1 - num2)
            elif token == "*":
                num2 = numStack.pop()
                num1 = numStack.pop()
                numStack.append(num1 * num2)
            elif token == "/":
                num2 = numStack.pop()
                num1 = numStack.pop()
                numStack.append(int(num1 / num2))
            else:
                numStack.append(int(token))
        return numStack.pop()