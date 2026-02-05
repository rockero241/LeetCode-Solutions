1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        ops = "+-/*"
5
6        for token in tokens:
7            if token not in ops:
8                stack.append(int(token))
9
10            else:
11                num2 = stack.pop()
12                num1 = stack.pop()
13
14                if token == "+":
15                    stack.append(num1 + num2)
16
17                elif token == "-":
18                    stack.append(num1 - num2)
19
20                elif token == "*":
21                    stack.append(num1 * num2)
22
23                elif token == "/":
24                    stack.append(int(num1 / num2))
25
26        return stack[-1] if stack else None