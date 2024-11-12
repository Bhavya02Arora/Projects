class Solution:
    def romanToInt(self, s: str) -> int:
        def check_three_ones_before_bigger(self, s, i, precedence_order):   
            if                                                                                                                                                                       

        roman_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000

        }
        number = 0
        precedence_order = ["M", "D", "C", "L", "X", "V", "I"]

        for i in range(len(s)):
            if s[]
            if s[i] == "I" and i < (len(s) - 3) and check_three_ones_after_bigger(s, i, precedence_order):
                i += 3
            if i < (len(s) - 2) and check_two_ones_before_bigger(s, i):
                i += 2
            if i < (len(s) - 1) and check_one_ones_before_bigger(s, i):
                i += 1
                
        