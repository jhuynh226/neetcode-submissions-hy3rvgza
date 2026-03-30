class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_stack = []
        bracket_map = {")" : "(", "]": "[", "}": "{"}

        for char in s:
            if char not in bracket_map:
                open_bracket_stack.append(char)
            elif char in bracket_map:
                if not open_bracket_stack:
                    return False
                elif open_bracket_stack[-1] == bracket_map[char]:
                    open_bracket_stack.pop()
                else:
                    return False

        if not open_bracket_stack:
            return True 
        else:
            return False
                    
        



