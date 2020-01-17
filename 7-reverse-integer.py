#Submitted-1, wrong answer in case reversed integer overflows

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        str_num = str(abs(x))
        reverse_num = str_num[::-1]
        if is_negative:
            return int(reverse_num) * -1
        else:
            return int(reverse_num)