class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            '}': '{',
            ']': '[',
            ')': '('
        } 

        open_bracket_stack = []

        for char in s:
            if char not in closing_brackets:
                open_bracket_stack.append(char)
            else:
                if not open_bracket_stack:
                    return False
                elif closing_brackets[char] != open_bracket_stack[-1]:
                    return False
                else:
                    open_bracket_stack.pop()
        
        return not open_bracket_stack




         

        