class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        bracket_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for char in s:
            if char in bracket_map:
                if open_brackets and open_brackets[-1] == bracket_map[char]:
                    open_brackets.pop()
                else:
                    return False
            else:
                open_brackets.append(char)
        
        return True if not open_brackets else False
