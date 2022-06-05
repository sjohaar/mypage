class Solution(object):
    sym_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    exception_map = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        prev = None
        for curr in s:
            if prev:
                if prev + curr in exception_map:
                    num = num + exception_map[prev + curr]
                    prev = None
                else:
                    num = num + sym_map[prev]
                    prev = curr
            else:
                prev = curr
        if prev:
            num = num + sym_map[prev]

print(Solution().romanToInt("IV"))