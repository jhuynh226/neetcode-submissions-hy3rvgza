class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_string = ''

        for digit in digits:     
            digit_string += str(digit) 
        
        new_digit_num = int(digit_string)
        new_digit_num += 1

        new_digit_string = str(new_digit_num)

        digit_list = []
        for digit in new_digit_string:
            digit_list.append(int(digit))
        
        return digit_list
