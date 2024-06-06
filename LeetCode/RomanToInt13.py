class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        single = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        combo = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

        total = 0

        for i in range(len(s)):
            if s[0:2] in combo:
                total += combo[s[0:2]]
                s = s[2:]
            else:
                if s[0:1] in single: 
                    total += single[s[0:1]]
                    s = s[1:]
                else:
                    pass
        return total

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        single = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        combo = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

        total = 0

        for i in range(len(s)):
            if s[0:2] in combo:
                total += combo[s[0:2]]
                s = s[2:]
            else:
                if s[0:1] in single: 
                    total += single[s[0:1]]
                    s = s[1:]
                else:
                    pass
        return total

print(romanToInt("III"))