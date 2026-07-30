class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"]":"[",
                    "}": "{",
                    ")": "(",
                    }

        stack = []

        for n in s:
            if stack and n in mapping and stack[-1] == mapping[n]:
                stack.pop()
            else:
                stack.append(n)
        
        return not stack