class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        cur = 0

        while carry:
            if cur == len(digits):
                digits.append(1)
                carry = 0
                continue 

            if digits[cur] != 9:
                digits[cur] += 1
                carry = 0
                continue

            digits[cur] = 0
            cur += 1
        
        return digits[::-1]