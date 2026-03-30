class Solution:
    def isValid(self, s: str) -> bool:
        #()
        #([{}])
        #()[({})]

        closing_brackets = ['}', ')', ']']

        open_stack = []

        for char in s:
            if char not in closing_brackets:
                open_stack.append(char)

            else:
                if not open_stack:
                    return False

                if char == '}' and open_stack[-1] == '{':
                    open_stack.pop()
                elif char == ']' and open_stack[-1] == '[':
                    open_stack.pop()
                elif char == ')' and open_stack[-1] == '(':
                    open_stack.pop()
                else:
                    return False

        if open_stack:
            return False
        else:
            return True