#Submitted-1, wrong answer in case reversed integer overflows
#Submitted-2, 44ms, Fix in case reversed integer overflows

class Solution:
    def reverse(self, x: int) -> int:
        multiplier = -1 if x < 0 else 1
        str_num = str(abs(x))
        reverse_num = int(str_num[::-1]) * multiplier
        return reverse_num if reverse_num.bit_length() <= 31 else 0